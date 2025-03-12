import pytest_asyncio

from ampay.connections import Base, engine, redis


@pytest_asyncio.fixture
async def clean_repositories():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest_asyncio.fixture
async def clean_cache():
    await redis.flushdb()
