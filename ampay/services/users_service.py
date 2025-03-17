from uuid import UUID, uuid4

from sqlalchemy.ext.asyncio import AsyncSession

from ampay.dependencies import cache
from ampay.schemas.users_schemas import SUser
from ampay.dependencies.cache import user_to_dict
from ampay.repositories.users_repositories import ClientsRepository, AdminsRepository
from ampay.repositories.passwords_repository import PasswordsRepository
from ampay.dependencies.auth import get_password_hash, verify_password


class UsersService:
    @classmethod
    async def register(cls, session: AsyncSession, **user_data) -> UUID:
        password = get_password_hash(user_data.pop("password"))
        role = user_data.pop("role")

        user_id = uuid4()
        passwordId = uuid4()

        await PasswordsRepository.add(session, id=passwordId, password=password)

        if role == "client":
            await ClientsRepository.add(
                session, 
                id=user_id, 
                passwordId=passwordId, 
                **user_data
            )
        if role == "admin":
            await AdminsRepository.add(
                session, 
                id=user_id, 
                passwordId=passwordId, 
                **user_data
            )

        return user_id

    @classmethod
    async def find(cls, session: AsyncSession, **user_data):
        role = user_data.pop("role")
        user_id = user_data.get("id")
        
        if user_id:
            user = await cache.get("Users", user_id)

            if user:
                return SUser(**user)

        if role == "client":
            user = await ClientsRepository.get(session, **user_data)
        if role == "admin":
            user = await AdminsRepository.get(session, **user_data)

        if user:
            dict_user = user_to_dict(user)
            await cache.add("Users", dict_user.get("id"), dict_user)

        return user

    @classmethod
    async def get_pass(cls, session: AsyncSession, **user_data) -> str:
        value = await PasswordsRepository.get(session, **user_data)
        return value.password
