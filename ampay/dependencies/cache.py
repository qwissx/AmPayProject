import json

from ampay.connections import redis


async def add(typ: str, key: str, data: str | dict, exp=360):
    key_val = f"{typ}:{key}"

    if isinstance(data, dict):
        data = json.dumps(data)

    await redis.set(key_val, data)
    await redis.expire(key_val, exp)


async def get(typ: str, key: str):
    key_val = f"{typ}:{key}"

    value = await redis.get(key_val)

    if not value:
        return None

    await redis.expire(key_val, 360)

    return json.loads(value.decode())


async def rem(typ: str, key: str):
    key_val = f"{typ}:{key}"

    await redis.delete(key_val)
