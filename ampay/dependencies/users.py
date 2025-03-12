from fastapi import Depends, Request

from ampay.connections import session_getter
from sqlalchemy.ext.asyncio import AsyncSession
from ampay.exceptions import AuthExc


def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise AuthExc.UserNotAuthorized
    return token


async def get_current_user(
    token: str = Depends(get_token),
    session: AsyncSession = Depends(session_getter),
):
    pass