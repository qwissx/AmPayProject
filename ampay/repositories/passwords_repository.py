from ampay.repositories.base_repository import BaseRepository
from ampay.models.passwordsModel import Passwords

class PasswordsRepository(BaseRepository):
    model = Passwords
