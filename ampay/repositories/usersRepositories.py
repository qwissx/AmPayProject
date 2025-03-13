from ampay.repositories.baseRepository import BaseRepository
from ampay.models.usersModel import Clients

class ClientsRepository(BaseRepository):
    model = Clients


class AdminsRepository(BaseRepository):
    model = None
