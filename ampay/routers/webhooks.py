from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ampay.connections import database_session
from ampay.services.payments_service import PayInService, RefundService
from ampay.schemas import webhooks_schemas as wS


hook_router = APIRouter(prefix="/webhook", tags=["Webhooks for partners"])


@hook_router.post(path="/rz/payin")
async def rz_confirm_payin(
    body: wS.SPayInWebhook,
    session: AsyncSession = Depends(database_session),
):
    await PayInService.update_state(session, body.id, body.state)
    await session.commit()


@hook_router.post(path="/rz/refund")
async def rz_confirm_refund(
    body: wS.SRefundWebhook,
    session: AsyncSession = Depends(database_session),
):
    await RefundService.update_state(session, body.id, body.state)
    await session.commit()
