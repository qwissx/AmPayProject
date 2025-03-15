from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ampay.models.paymentsModel import Payments
from ampay.repositories.baseRepository import BaseRepository


class PaymentsRepository(BaseRepository):
    model = Payments

    @classmethod
    async def getPag(cls, session: AsyncSession, offset: int, limit: int, **filter_by):
        query = select(cls.model).filter_by(**filter_by)

        if offset and limit:
            query.offset(offset).limit(limit)

        payments = await session.execute(query)

        return payments.scalars().all()