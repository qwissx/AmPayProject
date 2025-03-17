from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ampay.models.payments_model import PayIn, PayOut
from ampay.repositories.base_repository import BaseRepository


class PayInRepository(BaseRepository):
    model = PayIn

    @classmethod
    async def get_pag(cls, session: AsyncSession, offset: int, limit: int, **filter_by):
        query = select(cls.model).filter_by(**filter_by)

        if offset and limit:
            query.offset(offset).limit(limit)

        payments = await session.execute(query)

        return payments.scalars().all()


class PayOutRepository(BaseRepository):
    model = PayOut
