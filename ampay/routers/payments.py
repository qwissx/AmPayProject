from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ampay.connections import database_session
from ampay.dependencies.users import get_current_user, admin_require
from ampay.schemas import users_schemas as uS
from ampay.schemas import payments_schemas as pS
from ampay.services.payments_service import PaymentsService
from ampay.repositories.payments_repository import PaymentsRepository
from ampay.dependencies.partner import CheckStatus


pay_router = APIRouter(prefix="/payments", tags=["Payments"])


@pay_router.post(path="/", status_code=status.HTTP_201_CREATED)
async def create_payment(
    payment: pS.SPaymentCreate,
    user: uS.SUser = Depends(get_current_user),
    session: AsyncSession = Depends(database_session),
) -> pS.SPaymentDisplay:
    payment = await PaymentsService.register(session, user.id, **payment.model_dump())

    await session.commit()

    return payment


@pay_router.get("/test")
async def test(
    user: uS.SUser = Depends(get_current_user)
):
    await CheckStatus("123")


@pay_router.get(path="/")
async def pagination_payments(
    offset: int = 0,
    limit: int = 0,
    user: uS.SUser = Depends(get_current_user),
    session: AsyncSession = Depends(database_session),
) -> pS.SPaginationPayments:
    payments, totalCount = await PaymentsService.findPag(session, offset, limit, clientId=user.id)

    return {
        "payments": payments,
        "totalCount": totalCount,
        "currentCount": min(limit + offset, totalCount),
    }


@pay_router.get(path="/{payId}")
async def get_payment(
    payId: str, 
    session: AsyncSession = Depends(database_session),
) -> pS.SPaymentDisplay:
    payment = await PaymentsRepository.get(session, id=payId)

    return payment


@pay_router.delete(path="/{payId}")
async def del_payment(
    payId: str, 
    user: uS.SUser = Depends(admin_require),
    session: AsyncSession = Depends(database_session),
) -> dict[str, str]:
    await PaymentsService.delete(session, id=payId)

    await session.commit()

    return {"message": "Payment was successfully deleted"}
