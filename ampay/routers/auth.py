from fastapi import APIRouter, Depends, Response, status
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from ampay.schemas import usersSchemas as uS
from ampay.exceptions import AuthExc
from ampay.services.usersService import UsersService
from ampay.dependencies.auth import create_access_token
from ampay.connections import session_getter
from ampay.dependencies.users import get_current_user


reg_router = APIRouter(prefix="/auth", tags=["Authorization"])


@reg_router.post(path="/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    response: Response,
    user_data: uS.SUserAuth,
    session: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    if await UsersService.find(session, role=user_data.role, email=user_data.email):
        raise AuthExc.UserExist

    user_id = await UsersService.register(session, **user_data.model_dump())

    access_token = await create_access_token(
        {"sub": str(user_id), "role": user_data.role}
    )
    response.set_cookie("access_token", access_token, httponly=True)

    await session.commit()

    return {"message": "user was added successfully"}


@reg_router.get(path="/hui")
async def get(user: uS.SUserDisplay = Depends(get_current_user)):
    return {"username": user.username, "email": user.email}