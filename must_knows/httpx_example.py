import asyncio
from httpx import AsyncClient


async def main() -> None:
    client = AsyncClient(base_url="https://pokeapi.co/api/v2")

    # Two calls, one after another
    r1 = await client.get("/pokemon/ditto")
    print(f"r1: {r1.status_code}")  # 200
    # You can use 'request' for better configurability
    r2 = await client.request("GET", "/pokemon/jynx")
    print(f"r2: {r2.status_code}")  # 200

    # Two calls made asynchronously
    r3, r4 = await asyncio.gather(
        client.get("/pokemon/lucario"),
        client.get("/pokemon/snorlax"),
    )
    print(f"r3: {r3.status_code}")  # 200
    print(f"r4: {r4.status_code}")  # 200

    # Call resulting in 404 and raising an 'HTTPStatusError'
    r5 = await client.get("/pokemon/john-wick")
    print(f"r5: {r5.status_code}")  # 404
    r5.raise_for_status()


async def configurability_example() -> None:
    client = AsyncClient(
        base_url="https://pokeapi.co/api/v2",
        auth=("ash", "ketchum123"),
        cookies={"access_token": "Bearer PIKACHU"},
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )

    # All requests share the same configuration
    await client.get("/pokemon/ditto")
    await client.request("GET", "/pokemon/jynx")
    await client.get("/pokemon/snorlax")


if __name__ == "__main__":
    asyncio.run(configurability_example())
