from ampay.repositories.base_repository import BaseRepository
from ampay.models.users_model import Clients, Admins


class ClientsRepository(BaseRepository):
    model = Clients


class AdminsRepository(BaseRepository):
    model = Admins
