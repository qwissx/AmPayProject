from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from ampay.repositories.usersRepository import UsersRepository
from ampay.repositories.passwordsRepository import PasswordsRepository
from ampay.dependencies.auth import get_password_hash


class UsersService:
    @classmethod
    async def register(cls, session: AsyncSession, **user_data) -> UUID:
        value = user_data.pop("password")
        password = get_password_hash(value)

        user_id = await UsersRepository.add(session, **user_data)
        await PasswordsRepository.add(session, user_id=user_id, password=password)

        return user_id
