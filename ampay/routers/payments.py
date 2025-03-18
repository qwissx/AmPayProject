from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ampay.connections import database_session
from ampay.dependencies.users import get_current_user, admin_require
from ampay.schemas import users_schemas as uS
from ampay.schemas import payments_schemas as pS
from ampay.services.payments_service import PayInService, RefundService
from ampay.repositories.payments_repository import PayInRepository, RefundRepository


pay_router = APIRouter(prefix="/payments", tags=["Payments"])


@pay_router.post(path="/payin", status_code=status.HTTP_201_CREATED)
async def create_payin(
    payment: pS.SPayInCreate,
    user: uS.SUser = Depends(get_current_user),
    session: AsyncSession = Depends(database_session),
) -> pS.SPayInDisplay:
    payment = await PayInService.create(session, user.id, **payment.model_dump())

    await session.commit()

    return payment


@pay_router.post(path="/refund", status_code=status.HTTP_201_CREATED)
async def create_refund(
    payment: pS.SRefundCreate,
    user: uS.SUser = Depends(get_current_user),
    session: AsyncSession = Depends(database_session),
) -> pS.SRefundDisplay:
    payment = await RefundService.create(session, user.id, **payment.model_dump())

    await session.commit()

    return payment


@pay_router.get(path="/payin")
async def pagination_payin(
    offset: int = 0,
    limit: int = 0,
    user: uS.SUser = Depends(get_current_user),
    session: AsyncSession = Depends(database_session),
) -> pS.SPaginationPayIn:
    payments, total_count = await PayInService.find_pag(session, offset, limit, client_id=user.id)

    return {
        "payments": payments,
        "total_count": total_count,
        "current_count": min(limit + offset, total_count),
    }


@pay_router.get(path="/refund")
async def pagination_refund(
    offset: int = 0,
    limit: int = 0,
    user: uS.SUser = Depends(get_current_user),
    session: AsyncSession = Depends(database_session),
) -> pS.SPaginationRefund:
    payments, total_count = await RefundService.find_pag(session, offset, limit, client_id=user.id)

    return {
        "payments": payments,
        "total_count": total_count,
        "current_count": min(limit + offset, total_count),
    }


@pay_router.get(path="/payin/{pay_id}")
async def get_payin(
    pay_id: str, 
    session: AsyncSession = Depends(database_session),
) -> pS.SPayInDisplay:
    payment = await PayInRepository.get(session, id=pay_id)

    return payment


@pay_router.get(path="/refund/{refund_id}")
async def get_refund(
    refund_id: str, 
    session: AsyncSession = Depends(database_session),
) -> pS.SPayInDisplay:
    payment = await RefundRepository.get(session, id=refund_id)

    return payment


@pay_router.delete(path="/payin/{pay_id}")
async def del_payin(
    pay_id: str, 
    user: uS.SUser = Depends(admin_require),
    session: AsyncSession = Depends(database_session),
) -> dict[str, str]:
    await PayInService.delete(session, id=pay_id)

    await session.commit()

    return {"message": "Payment was successfully deleted"}


@pay_router.delete(path="/refund/{refund_id}")
async def del_refund(
    refund_id: str,
    user: uS.SUser = Depends(admin_require),
    session: AsyncSession = Depends(database_session),
) -> dict[str, str]:
    await RefundService.delete(session, id=refund_id)

    await session.commit()

    return {"message": "Refund was successfully deleted"}
