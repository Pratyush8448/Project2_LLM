import httpx

async def test_httpx():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://www.google.com")
        print(response.status_code)

import asyncio
asyncio.run(test_httpx())
