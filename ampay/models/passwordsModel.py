from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column, relationship

from ampay.connections import Base


class Passwords(Base):
    __tablename__ = "passwords"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    password: Mapped[str] = mapped_column(nullable=False)

    client_password = relationship("Clients", back_populates="password")
