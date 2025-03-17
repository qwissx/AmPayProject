from ampay.repositories.base_repository import BaseRepository
from ampay.models.usersModel import Clients, Admins


class ClientsRepository(BaseRepository):
    model = Clients


class AdminsRepository(BaseRepository):
    model = Admins
