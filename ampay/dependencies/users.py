from fastapi import Depends, Request
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from ampay.exceptions import AuthExc
from ampay.connections import database_session
from ampay.dependencies.auth import check_access_token, authenticate_user
from ampay.services.users_service import UsersService
from ampay.settings import settings as st


def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise AuthExc.UserNotAuthorized
    return token


async def get_current_user(
    token: str = Depends(get_token),
    session: AsyncSession = Depends(database_session),
):
    try:
        payload = jwt.decode(token, st.secret, st.hash)
    except JWTError as e:
        raise AuthExc.UserNotAuthorized

    check_access_token(payload)

    user = await UsersService.find(session, id=payload.get("sub"), role=payload.get("role"))

    if not user:
        raise AuthExc.UserDoesNotExist

    await authenticate_user(user.id, payload.get("role"))

    return user


async def admin_require(user = Depends(get_current_user)):
    if user.role != "admin":
        raise AuthExc.HaveNoRights

    return user
