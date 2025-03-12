from ampay.repositories.baseRepository import BaseRepository
from ampay.models.usersModel import Users

class UsersRepository(BaseRepository):
    model = Users
