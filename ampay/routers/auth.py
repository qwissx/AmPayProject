from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from ampay.schemas import usersSchemas as uS
from ampay.repositories.usersRepository import UsersRepository
from ampay.exceptions import AuthExc
from ampay.services.usersService import UsersService
from ampay.dependencies.auth import create_access_token


reg_router = APIRouter(prefix="/auth", tags=["Authorization"])


@reg_router.post(path="/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    response: Response,
    user_data: uS.SUserAuth,
    session: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    if await UsersRepository.get(session, email=user_data.email):
        raise AuthExc.UserExist

    user_id = await UsersService.register(session, **user_data.model_dump())

    access_token = await create_access_token(
        {"sub": str(user_id), "role": user_data.role}
    )
    response.set_cookie("access token", access_token, httponly=True)

    return {"message": "user was added successfully"}
