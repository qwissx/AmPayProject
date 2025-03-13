from datetime import datetime, timedelta
from uuid import uuid4

from passlib.context import CryptContext
from jose import jwt

from ampay.dependencies import cache
from ampay.settings import settings as st
from ampay.exceptions import AuthExc


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_pass, hashed_pass) -> bool:
    return pwd_context.verify(plain_pass, hashed_pass)


async def generate_access_key(user_id: str, role: str):
    access_key = {"key": str(uuid4()), "role": role}

    await cache.add("AccessKey", user_id, access_key, 1800)

    return access_key


async def create_access_token(data: dict):
    access_key = await generate_access_key(data.get("sub"), data.get("role"))

    encoded_jwt = jwt.encode(data, st.secret, st.hash)

    return encoded_jwt


def check_access_token(payload: dict):
    user_id = payload.get("sub")
    if not user_id:
        raise AuthExc.TokenIdNotValid

    role = payload.get("role")
    if not role:
        raise AuthExc.TokenRoleNotValid


async def authenticate_user(user_id: str, expected_role: str):
    access_key = await cache.get("AccessKey", user_id)

    if not access_key:
        raise AuthExc.UserNotAuthorized

    actual_role = access_key.get("role")
    if actual_role != expected_role:
        raise AuthExc.HaveNoRights
