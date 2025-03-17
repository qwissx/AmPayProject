from typing import Literal

from fastapi import Depends
from aiohttp import ClientSession, http

from ampay.connections import client_session as session
from ampay.settings import settings as st
from ampay.schemas import payments_schemas as pS


async def create_request(
    url: str,
    method: Literal["get", "post"],
    url_tail: str | None = None,
    params: dict | None = None, 
):
    if url_tail:
        url = url + "/" + url_tail

    request_data = {}

    if params:
        request_data.update({"params": params})

    if method == "get":
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {st.partner_api_key}"
        }
        request_data.update(headers)
        return await session.get(url, **request_data)
    if method == "post":
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Bearer {st.partner_api_key}"
        }
        request_data.update(headers)
        return await session.post(url, **request_data)


async def create_payin(
    payment_type: pS.Type, 
    paymet_method: pS.Method, 
    amount: float | str, 
    currency: pS.Currency,
):
    request = await create_request(
        url="payments",
        method="post"

    )
    json_response = await request.json()

    print(json_response)


async def check_status(payment_id: str):
    request = await create_request(
        url="payments",
        method="get",
        url_tail=payment_id,
    )

    json_response = await request.json()
    
    return json_response
