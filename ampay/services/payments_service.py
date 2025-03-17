from uuid import uuid4, UUID
from datetime import datetime
from copy import deepcopy
from typing import Literal
import abc

from sqlalchemy.ext.asyncio import AsyncSession

from ampay.exceptions import SQLAlchExc
from ampay.repositories.payments_repository import PayInRepository, PayOutRepository
from ampay.dependencies import rz_partner as RZPartner


class BasePaymentsService(abc.ABC):
    PayRepository = None

    @classmethod
    async def find_pag(cls, session: AsyncSession, offset, limit, **filter_by):
        payments = await cls.PayRepository.get_pag(session, offset, limit, **filter_by)
        total_count = await cls.PayRepository.count(session, **filter_by)

        return payments, total_count

    @classmethod
    async def delete(cls, session: AsyncSession, **filter_by):
        if not await cls.PayRepository.get(session, **filter_by):
            raise SQLAlchExc.PaymentDoesNotExist

        await cls.PayRepository.rem(session, **filter_by)


class PayInService(BasePaymentsService):
    PayRepository = PayInRepository

    @classmethod
    async def create(cls, session: AsyncSession, user_id: UUID, **payment_data):
        """payment_data
            reference_id: str | None = None
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

        await PayInRepository.add(
            session,
            id=payment_id,
            clientId=user_id,
            created_at=current_time,
            state="COMPLETED",
            **payment,
        )

        payment.update(
            id=payment_id,
            clientId=user_id,
            created_at=current_time,
            state="COMPLETED",
        )

        return payment


class PayOutService(BasePaymentsService):
    PayRepository = PayOutRepository

    @classmethod
    async def create(cls, session: AsyncSession, user_id: UUID, **payment_data):
        """payment_data
            reference_id: str | None = None
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

        await PayInRepository.add(
            session,
            id=payment_id,
            clientId=user_id,
            created_at=current_time,
            state="COMPLETED",
            **payment,
        )

        payment.update(
            id=payment_id,
            clientId=user_id,
            created_at=current_time,
            state="COMPLETED",
        )

        return payment
