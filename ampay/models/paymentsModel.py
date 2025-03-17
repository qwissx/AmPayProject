from uuid import UUID
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from ampay.connections import Base
from ampay.schemas import payments_schemas as pS


class Payments(Base):
    __tablename__ = "payments"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    clientId: Mapped[UUID] = mapped_column(ForeignKey("clients.id"), nullable=False)
    referenceId: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[pS.Type] = mapped_column(nullable=False)
    method: Mapped[pS.Method] = mapped_column(nullable=False)
    amount: Mapped[float] = mapped_column(nullable=False)
    currency: Mapped[pS.Currency] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    createdAt: Mapped[datetime] = mapped_column(nullable=False)
    state: Mapped[pS.State] = mapped_column(nullable=False)

    user = relationship("Clients", back_populates="payments")
