import asyncio
import time
import httpx
from app.config import HEADERS, MONITORS

STATUS: dict[str, dict] = {}


async def monitor(name: str, url: str, interval: int, client: httpx.AsyncClient):
    while True:
        timestamp = time.strftime("%H:%M:%S")
        try:
            code = (await client.get(url, headers=HEADERS, timeout=10)).status_code
        except Exception as e:
            code = f"FAIL ({e})"
        STATUS[name] = {"code": code, "time": timestamp}
        await asyncio.sleep(interval)


def status() -> dict:
    return {
        name: {
            "url": data["url"],
            "interval": data["interval"],
            "status": STATUS.get(name, {}).get("code", "PENDING"),
            "last_checked": STATUS.get(name, {}).get("time", "-"),
        }
        for name, data in MONITORS.items()
    }
