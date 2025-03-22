from typing import Literal
from uuid import UUID

from fastapi import Depends
from aiohttp import ClientSession, http

from ampay.connections import client_session as session
from ampay.settings import settings as st
from ampay.schemas import payments_schemas as pS
from ampay.connections import broker


async def create_request(
    url: str,
    method: Literal["get", "post"],
    url_tail: str | None = None,
    json: dict | None = None,
    params: dict | None = None,
):
    if url_tail:
        url = url + "/" + url_tail

    request_data = {}

    if params:
        request_data.update({"params": params})
    if json:
        request_data.update({"json": json})

    if method == "get":
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {st.partner_api_key}"
        }
        request_data.update({"headers": headers})
        return await session.get(url, **request_data)
    if method == "post":
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Bearer {st.partner_api_key}"
        }
        request_data.update({"headers": headers})
        return await session.post(url, **request_data)


@broker.task
async def create_payin(
    payment_type: pS.Type, 
    paymet_method: pS.Method, 
    amount: float | str, 
    currency: pS.Currency,
    count: int = 0,
    **params,
):
    json = {
        "paymentType": payment_type,
        "paymentMethod": paymet_method,
        "amount": amount,
        "currency": currency,
        "webhookUrl": st.webhook_url,
    }

    if params:
        json.update(params)

    request = await create_request(
        url="payments",
        method="post",
        json=json,
    )
    json_response = await request.json()

    status = json_response.get("status")

    if status == 200:
        return json_response.get("result")
    if (status in [400, 401]) or count >= 4:
        return None
    else:
        create_payin.apply_async(
            countdown=2, 
            kwargs={
                "payment_type": payment_type,
                "paymet_method": paymet_method, 
                "amount": amount,
                "currency": currency,
                "count": count + 1,
                "params": params,
            }
        )


@broker.task
async def create_refund(
    amount: float | str,
    currency: pS.Currency,
    parent_payment_id: UUID,
    count: int = 0,
    **params
):
    json = {
        "amount": amount,
        "currency": currency,
        "parent_payment_id": parent_payment_id,
        "webhookUrl": st.webhook_url,
    }

    if params:
        json.update(params)

    request = await create_request(
        url="refund/",
        method="post",
        json=json,
    )
    json_response = await request.json()

    status = json_response.get("status")

    if status == 200:
        return json_response.get("result")
    elif (status in [400, 401]) or count == 4:
        return None
    else:
        create_payin.apply_async(
            countdown=2, 
            kwargs={
                "parent_payment_id": parent_payment_id,
                "amount": amount,
                "currency": currency,
                "count": count + 1,
                "params": params,
            }
        )


@broker.task
async def check_status(payment_id: str, count: int = 0):
    request = await create_request(
        url="payments",
        method="get",
        url_tail=payment_id,
    )

    json_response = await request.json()
    
    status = json_response.get("status")

    if status == 200:
        return json_response.get("result")
    elif (status in [401, 404]) or count == 4:
        return None
    else:
        create_payin.apply_async(
            countdown=2, 
            kwargs={
                "payment_id": payment_id,
                "count": count + 1,
            }
        )
