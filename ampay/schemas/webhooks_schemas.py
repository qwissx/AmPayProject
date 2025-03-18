from uuid import UUID

from pydantic import BaseModel

from ampay.schemas.payments_schemas import State


class SPayInWebhook(BaseModel):
    id: UUID
    state: State


class SRefundWebhook(BaseModel):
    id: UUID
    state: State
