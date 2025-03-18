from uuid import uuid4, UUID
from datetime import datetime
from copy import deepcopy
from typing import Literal

from sqlalchemy.ext.asyncio import AsyncSession

from ampay.exceptions import SQLAlchExc, RZExc
from ampay.repositories.payments_repository import PayInRepository, RefundRepository
from ampay.dependencies import rz_partner as RZPartner
from ampay.schemas.payments_schemas import State


class BasePaymentsService:
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

    @classmethod
    async def update_state(cls, session: AsyncSession, payment_id: UUID, new_state: State):
        await cls.PayRepository.update(session, payment_id, state=new_state)


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
        payment = deepcopy(payment_data)

        payment_type = payment_data.pop("type")
        paymet_method = payment_data.pop("method")
        amount = payment_data.pop("amount")
        currency = payment_data.pop("currency")

        response = await RZPartner.create_payin(
            payment_type=payment_type,
            paymet_method=paymet_method,
            amount=amount,
            currency=currency,
            **payment_data,
        )

        if not response:
            raise RZExc.BadPartnerResponse

        payment_id = response.get("id")
        created = datetime.fromisoformat(response.get("created"))
        state = response.get("state")

        await PayInRepository.add(
            session,
            id=payment_id,
            client_id=user_id,
            created_at=created,
            state=state,
            **payment,
        )

        payment.update(
            id=payment_id,
            client_id=user_id,
            created_at=created,
            state=state,
        )

        return payment


class RefundService(BasePaymentsService):
    PayRepository = RefundRepository

    @classmethod
    async def create(cls, session: AsyncSession, user_id: UUID, **payment_data):
        """payment_data
            reference_id: str | None = None
            type: Type | None = None
            method: Method | None = None
            amount: float
            currency: Currency
            description: str | None = None
            parent_payment_id: str
        """
        payment = deepcopy(payment_data)

        parent_payment_id = payment_data.pop("parent_payment_id")
        amount = payment_data.pop("amount")
        currency = payment_data.pop("currency")

        response = await RZPartner.create_refund(
            amount=amount,
            currency=currency,
            parent_payment_id=parent_payment_id,
            **payment_data,
        )

        if not response:
            raise RZExc.BadPartnerResponse

        payment_id = response.get("id")
        created = datetime.fromisoformat(response.get("created"))
        state = response.get("state")

        await PayInRepository.add(
            session,
            id=payment_id,
            client_id=user_id,
            created_at=created,
            state=state,
            **payment,
        )

        payment.update(
            id=payment_id,
            client_id=user_id,
            created_at=created,
            state=state,
        )

        return payment
