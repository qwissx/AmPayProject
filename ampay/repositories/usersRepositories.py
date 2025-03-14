from ampay.repositories.baseRepository import BaseRepository
from ampay.models.usersModel import Clients, Admins


class ClientsRepository(BaseRepository):
    model = Clients


class AdminsRepository(BaseRepository):
    model = Admins
