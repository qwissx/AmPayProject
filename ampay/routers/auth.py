from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from ampay.schemas import users_schemas as uS
from ampay.exceptions import AuthExc
from ampay.services.users_service import UsersService
from ampay.dependencies import auth as au
from ampay.connections import database_session
from ampay.dependencies.users import get_current_user


auth_router = APIRouter(prefix="/auth", tags=["Authorization"])


@auth_router.post(path="/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    response: Response,
    user_data: uS.SUserReg,
    session: AsyncSession = Depends(database_session),
) -> dict[str, str]:
    if await UsersService.find(session, role=user_data.role, email=user_data.email):
        raise AuthExc.UserExist

    user_id = await UsersService.register(session, **user_data.model_dump())

    access_token = await au.create_access_token(
        {"sub": str(user_id), "role": user_data.role}
    )
    response.set_cookie("access_token", access_token, httponly=True)

    await session.commit()

    return {"message": "User was added successfully"}


@auth_router.post(path="/login")
async def login_user(
    response: Response,
    user_data: uS.SUserLogIn,
    session: AsyncSession = Depends(database_session),
) -> dict[str, str]:
    user = await UsersService.find(session, role=user_data.role, email=user_data.email)
    
    if not user:
        raise AuthExc.UserDoesNotExist
    
    user_pass = await UsersService.get_pass(session, id=user.password_id)

    if not au.verify_password(user_data.password, user_pass):
        raise AuthExc.NotValidPass

    access_token = await au.create_access_token(
        {"sub": str(user.id), "role": user_data.role}
    )
    response.set_cookie("access_token", access_token, httponly=True)
    
    return {"message": "Access is open"}


@auth_router.delete(path="/logout")
async def logout_user(
    response: Response,
    user: uS.SUser = Depends(get_current_user),
    session: AsyncSession = Depends(database_session),
) -> dict[str, str]:
    await au.delete_access_token(user.id)
    response.delete_cookie("access_token")

    return {"message": "Access is denied"}
