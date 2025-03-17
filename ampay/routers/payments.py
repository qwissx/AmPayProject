from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ampay.connections import database_session
from ampay.dependencies.users import get_current_user, admin_require
from ampay.schemas import users_schemas as uS
from ampay.schemas import payments_schemas as pS
from ampay.services.payments_service import PaymentsService
from ampay.repositories.payments_repository import PaymentsRepository


pay_router = APIRouter(prefix="/payments", tags=["Payments"])


@pay_router.post(path="/payin", status_code=status.HTTP_201_CREATED)
async def create_payin(
    payment: pS.SPaymentCreate,
    user: uS.SUser = Depends(get_current_user),
    session: AsyncSession = Depends(database_session),
) -> pS.SPaymentDisplay:
    payment = await PaymentsService.payin(session, user.id, **payment.model_dump())

    await session.commit()

    return payment


@pay_router.post


@pay_router.get(path="/")
async def pagination_payments(
    offset: int = 0,
    limit: int = 0,
    user: uS.SUser = Depends(get_current_user),
    session: AsyncSession = Depends(database_session),
) -> pS.SPaginationPayments:
    payments, totalCount = await PaymentsService.find_pag(session, offset, limit, clientId=user.id)

    return {
        "payments": payments,
        "totalCount": totalCount,
        "currentCount": min(limit + offset, totalCount),
    }


@pay_router.get(path="/{pay_id}")
async def get_payment(
    pay_id: str, 
    session: AsyncSession = Depends(database_session),
) -> pS.SPaymentDisplay:
    payment = await PaymentsRepository.get(session, id=pay_id)

    return payment


@pay_router.delete(path="/{pay_id}")
async def del_payment(
    pay_id: str, 
    user: uS.SUser = Depends(admin_require),
    session: AsyncSession = Depends(database_session),
) -> dict[str, str]:
    await PaymentsService.delete(session, id=pay_id)

    await session.commit()

    return {"message": "Payment was successfully deleted"}
