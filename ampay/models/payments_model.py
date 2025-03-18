from uuid import UUID
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from ampay.connections import Base
from ampay.schemas import payments_schemas as pS


class PayIn(Base):
    __tablename__ = "rz_payin"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    client_id: Mapped[UUID] = mapped_column(ForeignKey("clients.id"), nullable=False)
    reference_id: Mapped[str] = mapped_column(nullable=True)
    type: Mapped[pS.Type] = mapped_column(nullable=False)
    method: Mapped[pS.Method] = mapped_column(nullable=False)
    amount: Mapped[float] = mapped_column(nullable=False)
    currency: Mapped[pS.Currency] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(nullable=False)
    state: Mapped[pS.State] = mapped_column(nullable=False)

    client = relationship("Clients", back_populates="payin")


class Refund(Base):
    __tablename__ = "rz_refund"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    client_id: Mapped[UUID] = mapped_column(ForeignKey("clients.id"), nullable=False)
    reference_id: Mapped[str] = mapped_column(nullable=True)
    type: Mapped[pS.Type] = mapped_column(nullable=False)
    method: Mapped[pS.Method] = mapped_column(nullable=False)
    amount: Mapped[float] = mapped_column(nullable=False)
    currency: Mapped[pS.Currency] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    parent_payment_id: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(nullable=False)
    state: Mapped[pS.State] = mapped_column(nullable=False)

    client = relationship("Clients", back_populates="refund")
