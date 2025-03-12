from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column, relationship

from ampay.connections import Base


class UsersPasswords(Base):
    __tablename__ = "passwords"

    user_id: Mapped[UUID] = mapped_column(primary_key=True)
    password: Mapped[str] = mapped_column(nullable=False)

    user = relationship("Users", back_populates="password")
