from ampay.repositories.base_repository import BaseRepository
from ampay.models.passwords_model import Passwords

class PasswordsRepository(BaseRepository):
    model = Passwords
