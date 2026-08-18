import asyncio
import json
import time
import httpx
from app.config import HEADERS, MONITORS_FILE

STATUS: dict[str, dict] = {}


async def monitor(name: str, url: str, interval: int, client: httpx.AsyncClient):
    while True:
        timestamp = time.strftime("%H:%M:%S")
        try:
            res = await client.get(url, headers=HEADERS, timeout=10)
            code, reason = res.status_code, res.reason_phrase
        except Exception as e:
            code, reason = f"FAIL ({e})", ""
        STATUS[name] = {"code": code, "time": timestamp}
        print(f"[{timestamp}] {name}: {code} {reason}".strip())
        await asyncio.sleep(interval)


def status() -> dict:
    monitors = json.loads(MONITORS_FILE.read_text(encoding="utf-8")) if MONITORS_FILE.exists() else {}
    return {
        name: {
            "url": data["url"],
            "interval": data["interval"],
            "status": STATUS.get(name, {}).get("code", "PENDING"),
            "last_checked": STATUS.get(name, {}).get("time", "-"),
        }
        for name, data in monitors.items()
    }
