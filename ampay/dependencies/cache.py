import json

from ampay.connections import redis
from ampay.models.users_model import Clients, Admins


def user_to_dict(user: Clients | Admins) -> dict:
    if isinstance(user, Clients):
        role = "client"
    if isinstance(user, Admins):
        role = "admin"

    user = user.__dict__
    user.pop("_sa_instance_state")

    user["id"] = str(user.get("id"))
    user["password_id"] = str(user.get("password_id"))
    
    user.update({"role": role})

    return user


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

    return json.loads(value.decode())


async def rem(typ: str, key: str):
    key_val = f"{typ}:{key}"

    await redis.delete(key_val)
