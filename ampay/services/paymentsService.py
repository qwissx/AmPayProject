from uuid import uuid4, UUID
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from ampay.repositories.paymentsRepository import PaymentsRepository


class PaymentsService:
    @classmethod
    async def register(cls, session: AsyncSession, user_id: UUID, **payment_data):
        payment_id = uuid4()
        current_time = datetime.utcnow()

        # http request to partner

        await PaymentsRepository.add(
            session,
            id=payment_id,
            clientId=user_id,
            createdAt=current_time,
            state="COMPLETED",
            **payment_data,
        )

        payment_data.update(
            id=payment_id,
            clientId=user_id,
            createdAt=current_time,
            state="COMPLETED",
        )

        return payment_data

    @classmethod
    async def findPag(cls, session: AsyncSession, offset, limit, **filter_by):
        payments = await PaymentsRepository.getPag(session, offset, limit, **filter_by)
        totalCount = await PaymentsRepository.count(session, **filter_by)

        # возможно кешировать значения

        return payments, totalCount
