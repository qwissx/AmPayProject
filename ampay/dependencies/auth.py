from datetime import datetime, timedelta
from uuid import uuid5

from passlib.context import CryptContext
from jose import jwt

# from e_commerce.repositories import usersRepository as uR
from ampay.dependencies import cache
from ampay import settings as st
from ampay.exceptions import AuthExc


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_pass, hashed_pass) -> bool:
    return pwd_context.verify(plain_pass, hashed_pass)


async def generate_access_key(user_id: str, role: str):
    access_key = {"key": uuid5, "role": role}

    await cache.add("AccessKey", user_id, access_key, 1800)

    return access_key


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)

    access_key = await generate_access_key(data.get("id"), data.get("role"))

    to_encode.update({"exp": expire, "key": access_key})
    encoded_jwt = jwt.encode(to_encode, st.secret, st.hash)

    return encoded_jwt


def check_access_token(payload: dict):
    expire = payload.get("exp")
    if not expire or int(expire) < datetime.utcnow().timestamp():
        raise AuthExc.TokenTimeNotValid

    access_key = payload.get("key")
    if not access_key:
        raise AuthExc.TokenKeyNotValid

    role = payload.get("role")
    if not role:
        raise AuthExc.TokenRoleNotValid


async def authenticate_user(connection, user, password):
    if not user:
        raise AuthExc.UserDoesNotExist

    password_is_valid = verify_password(password, user.password)
    if not password_is_valid:
        raise AuthExc.NotValidPass

    return user
