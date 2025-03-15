from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ampay.connections import session_getter
from ampay.dependencies.users import get_current_user
from ampay.schemas import usersSchemas as uS
from ampay.schemas import paymentsSchemas as pS
from ampay.services.paymentsService import PaymentsService
from ampay.repositories.paymentsRepository import PaymentsRepository


pay_router = APIRouter(prefix="/payments", tags=["Payments"])


@pay_router.post(path="/", status_code=status.HTTP_201_CREATED)
async def create_payment(
    payment: pS.SPaymentCreate,
    user: uS.SUser = Depends(get_current_user),
    session: AsyncSession = Depends(session_getter),
) -> pS.SPaymentDisplay:
    payment = await PaymentsService.register(session, user.id, **payment.model_dump())

    await session.commit()

    return payment


@pay_router.get(path="/")
async def pagination_payments(
    offset: int = 0,
    limit: int = 0,
    user: uS.SUser = Depends(get_current_user),
    session: AsyncSession = Depends(session_getter),
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
    session: AsyncSession = Depends(session_getter),
) -> pS.SPaymentDisplay:
    payment = await PaymentsRepository.get(session, id=payId)

    return payment


@pay_router.delete(path="/{payId}")
async def del_payment(
    payId: str, 
    session: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    await PaymentsRepository.rem(session, id=payId)

    await session.commit()

    return {"message": "payment was successfully deleted"}
