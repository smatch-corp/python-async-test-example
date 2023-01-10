import time
import httpx
import asyncio

import pytest

URL = "https://apitest.smatch.kr/api/ping"


@pytest.mark.asyncio
def test_ping1():
    client1 = httpx.Client()

    start = time.time()
    responses = [client1.get(URL) for _ in range(300)]
    print(f"\ntest_ping1 - API 호출 시간: {time.time() - start}")
    for response in responses:
        assert response.status_code == 307


@pytest.mark.asyncio
def test_ping2():
    clients = [httpx.Client() for _ in range(5)]

    start = time.time()
    responses = [clients[i % 5].get(URL) for i in range(300)]
    print(f"\ntest_ping2 - API 호출 시간: {time.time() - start}")
    for response in responses:
        assert response.status_code == 307


@pytest.mark.asyncio
async def test_async_ping1():
    a_client1 = httpx.AsyncClient()

    start = time.time()
    responses = await asyncio.gather(*[a_client1.get(URL) for _ in range(300)])
    print(f"\ntest_async_ping1 - API 호출 시간: {time.time() - start}")
    for response in responses:
        assert response.status_code == 307


@pytest.mark.asyncio
async def test_async_ping2():
    a_clients = [httpx.AsyncClient() for _ in range(5)]

    start = time.time()
    responses = await asyncio.gather(
        *[a_clients[i % 5].get(URL) for i in range(300)],
    )
    print(f"\ntest_async_ping2 - API 호출 시간: {time.time() - start}")
    for response in responses:
        assert response.status_code == 307
