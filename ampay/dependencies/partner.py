from typing import Literal

from fastapi import Depends
from aiohttp import ClientSession, http

from ampay.connections import client_session as session
from ampay.settings import settings as st


async def create_request(
    url: str,
    method: Literal["get", "post"],
    headers: dict, 
    url_tail: str | None = None,
    params: dict | None = None, 
):
    if url_tail:
        url = url + "/" + url_tail

    request_data = {"headers": headers}

    if params:
        request_data.update({"params": params})

    if method == "get":
        return await session.get(url, **request_data)
    if method == "post":
        return await session.post(url, **request_data)


async def CreatePayIn():
    request = await create_request("")
    json_response = await request.json()

    print(json_response)


async def CheckStatus(paymentId: str):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {st.partner_api_key}"
    }

    request = await create_request(
        url="payments",
        method="get",
        headers=headers,
        url_tail=paymentId,
    )

    json_response = await request.json()
    
    return json_response
