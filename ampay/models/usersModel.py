from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column, relationship

from ampay.connections import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)

    password = relationship("Passwords", back_populates="user")
