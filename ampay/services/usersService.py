from uuid import UUID, uuid4

from sqlalchemy.ext.asyncio import AsyncSession

from ampay.repositories.usersRepositories import ClientsRepository
from ampay.repositories.passwordsRepository import PasswordsRepository
from ampay.dependencies.auth import get_password_hash


class UsersService:
    @classmethod
    async def register(cls, session: AsyncSession, **user_data) -> UUID:
        password = get_password_hash(user_data.pop("password"))

        user_id = uuid4()
        password_id = uuid4()

        role = user_data.pop("role")

        await PasswordsRepository.add(session, id=password_id, password=password)

        if role == "client":
            await ClientsRepository.add(
                session, 
                id=user_id, 
                password_id=password_id, 
                **user_data
            )
        if role == "admin":
            pass

        return user_id


    @classmethod
    async def find(cls, session: AsyncSession, **user_data) -> UUID:
        role = user_data.pop("role")

        if role == "client":
            return await ClientsRepository.get(session, **user_data)
        if role == "admin":
            pass
