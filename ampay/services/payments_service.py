from uuid import uuid4, UUID
from datetime import datetime
from copy import deepcopy

from sqlalchemy.ext.asyncio import AsyncSession

from ampay.exceptions import SQLAlchExc
from ampay.repositories.payments_repository import PaymentsRepository
from ampay.dependencies import rz_partner as RZPartner


class PaymentsService:
    @classmethod
    async def payin(cls, session: AsyncSession, user_id: UUID, **payment_data):
        """payment_data
            referenceId: str | None = None
            type: Type = Type.DEPOSIT
            method: Method = Method.BASIC_CARD
            amount: float
            currency: Currency
            description: str | None = None
        """
        payment_id = uuid4()
        current_time = datetime.utcnow()

        payment = deepcopy(payment_data)

        payment_type = payment_data.pop("type")
        paymet_method = payment_data.pop("method")
        amount = payment_data.pop("amount")
        currency = payment_data.pop("currency")

        await RZPartner.create_payin(
            payment_type=payment_type,
            paymet_method=paymet_method,
            amount=amount,
            currency=currency,
            **payment_data,
        )

        await PaymentsRepository.add(
            session,
            id=payment_id,
            clientId=user_id,
            createdAt=current_time,
            state="COMPLETED",
            **payment,
        )

        payment.update(
            id=payment_id,
            clientId=user_id,
            createdAt=current_time,
            state="COMPLETED",
        )

        return payment

    @classmethod
    async def find_pag(cls, session: AsyncSession, offset, limit, **filter_by):
        payments = await PaymentsRepository.getPag(session, offset, limit, **filter_by)
        totalCount = await PaymentsRepository.count(session, **filter_by)

        return payments, totalCount

    @classmethod
    async def delete(cls, session: AsyncSession, **filter_by):
        if not await PaymentsRepository.get(session, **filter_by):
            raise SQLAlchExc.PaymentDoesNotExist

        await PaymentsRepository.rem(session, **filter_by)
