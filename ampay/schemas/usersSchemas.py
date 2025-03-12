from pydantic import BaseModel, EmailStr
from enum import Enum


class Role(str, Enum):
    ADMIN = "admin"
    CLIENT = "client"


class SUserAuth(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Role = Role.CLIENT
