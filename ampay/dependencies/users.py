from fastapi import Depends, Request
from jose import jwt, JWTError

from sqlalchemy.ext.asyncio import AsyncSession

from ampay.exceptions import AuthExc
from ampay.connections import session_getter
from ampay.dependencies.auth import check_access_token
from ampay.repositories.usersRepository import UsersRepository


def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise AuthExc.UserNotAuthorized
    return token


async def get_current_user(
    token: str = Depends(get_token),
    session: AsyncSession = Depends(session_getter),
):
    try:
        payload = jwt.decode(token, st.secret, st.hash)
    except JWTError as e:
        raise AuthExc.UserNotAuthorized

    check_access_token(payload)

    user = UsersRepository.get(session, id=payload.get("sub"))

    if not user:
        raise AuthExc.UserDoesNotExist