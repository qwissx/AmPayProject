from ampay.repositories.baseRepository import BaseRepository
from ampay.models.passwordsModel import Passwords

class PasswordsRepository(BaseRepository):
    model = Passwords
