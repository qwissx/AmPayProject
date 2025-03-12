from uuid import uuid5, UUID

from sqlalchemy import delete, insert, select, func
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository():
    model_name = None

    @classmethod
    async def add(cls, session: AsyncSession, **data) -> UUID:
        new_id = uuid5()
        query = insert(cls.model_name).values(id=new_id, **data)
        await session.execute(query)
        return new_id

    @classmethod
    async def get(cls, session: AsyncSession, **filter_by):
        query = select(cls.model_name).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def rem(cls, session: AsyncSession, **filter_by) -> None:
        query = delete(cls.model_name).filter_by(**filter_by)
        await session.execute(query)

    @classmethod
    async def count(cls, session: AsyncSession, **filter_by) -> int:
        query = select(func.count()).select_from(cls.model_name).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalar_one()
