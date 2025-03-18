from typing import Literal
from uuid import UUID

from fastapi import Depends
from aiohttp import ClientSession, http

from ampay.connections import client_session as session
from ampay.settings import settings as st
from ampay.schemas import payments_schemas as pS


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


async def create_payin(
    payment_type: pS.Type, 
    paymet_method: pS.Method, 
    amount: float | str, 
    currency: pS.Currency,
    **params,
):
    json = {
        "paymentType": payment_type,
        "paymentMethod": paymet_method,
        "amount": amount,
        "currency": currency,
        "webhookUrl": st.webhook_url + "/rz/payin",
    }

    if params:
        json.update(params)

    request = await create_request(
        url="payments",
        method="post",
        json=json,
    )
    json_response = await request.json()

    if json_response.get("status") == 200:
        return json_response.get("result")
    
    return None


async def create_refund(
    amount: float | str,
    currency: pS.Currency,
    parent_payment_id: UUID,
    **params
):
    json = {
        "amount": amount,
        "currency": currency,
        "parent_payment_id": parent_payment_id,
    }

    if params:
        json.update(params)

    request = await create_request(
        url="refund/",
        method="post",
        json=json,
    )
    json_response = await request.json()

    if json_response.get("status") == 200:
        return json_response.get("result")
    
    return None


async def check_status(payment_id: str):
    request = await create_request(
        url="payments",
        method="get",
        url_tail=payment_id,
    )

    json_response = await request.json()
    
    return json_response
