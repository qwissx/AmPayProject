from typing import AsyncGenerator

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from redis.asyncio import Redis

from ampay.settings import settings as st


engine = create_async_engine(st.db_url, poolclass=NullPool)


async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def session_getter() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
    

redis = Redis(host=st.redis_host, port=st.redis_port, db=0)
