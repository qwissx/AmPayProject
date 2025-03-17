from enum import Enum
from uuid import UUID

from pydantic import BaseModel, EmailStr


class Role(str, Enum):
    ADMIN = "admin"
    CLIENT = "client"


class SUserLogIn(BaseModel):
    email: EmailStr
    password: str
    role: Role = Role.CLIENT


class SUserReg(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Role = Role.CLIENT


class SUserDisplay(BaseModel):
    username: str
    email: EmailStr


class SUser(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    role: Role
