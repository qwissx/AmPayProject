from uuid import UUID, uuid4

from sqlalchemy.ext.asyncio import AsyncSession

from ampay.repositories.usersRepositories import ClientsRepository, AdminsRepository
from ampay.repositories.passwordsRepository import PasswordsRepository
from ampay.dependencies.auth import get_password_hash, verify_password


class UsersService:
    @classmethod
    async def register(cls, session: AsyncSession, **user_data) -> UUID:
        password = get_password_hash(user_data.pop("password"))
        role = user_data.pop("role")

        user_id = uuid4()
        password_id = uuid4()

        await PasswordsRepository.add(session, id=password_id, password=password1)

        if role == "client":
            await ClientsRepository.add(
                session, 
                id=user_id, 
                password_id=password_id, 
                **user_data
            )
        if role == "admin":
            await AdminsRepository.add(
                session, 
                id=user_id, 
                password_id=password_id, 
                **user_data
            )

        return user_id


    @classmethod
    async def find(cls, session: AsyncSession, **user_data):
        role = user_data.pop("role")

        if role == "client":
            return await ClientsRepository.get(session, **user_data)
        if role == "admin":
            return await AdminsRepository.get(session, **user_data)


    @classmethod
    async def get_pass(cls, session: AsyncSession, **user_data) -> str:
        value = await PasswordsRepository.get(session, **user_data)
        return value.password
