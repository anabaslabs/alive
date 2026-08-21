import asyncio
import json
import time
import httpx
from app.config import HEADERS, KD_HF_TOKEN, MONITORS_FILE, SR_HF_TOKEN, TIMEOUT

STATUS: dict[str, dict] = {}


def get_hf_info(url: str) -> tuple[str | None, str | None]:
    if ".hf.space" in url:
        domain = url.split("://")[-1].split(".hf.space")[0]
        if "-" in domain:
            user, space = domain.split("-", 1)
            token = KD_HF_TOKEN if "itskdhere" in user else SR_HF_TOKEN if "saptarshiroy39" in user else None
            return f"{user}/{space}", token
    return None, None


async def monitor(name: str, url: str, interval: int, client: httpx.AsyncClient):
    repo_id, token = get_hf_info(url)
    headers = {**HEADERS, "Authorization": f"Bearer {token}"} if token else HEADERS

    while True:
        timestamp = time.strftime("%H:%M:%S")
        try:
            res = await client.get(url, headers=headers, timeout=TIMEOUT)
            code, reason = res.status_code, res.reason_phrase
        except Exception as e:
            err = str(e).strip() or type(e).__name__
            code, reason = f"FAIL ({err})", ""

        if code == 503 and repo_id and token:
            try:
                await client.post(
                    f"https://huggingface.co/api/spaces/{repo_id}/restart",
                    headers={"Authorization": f"Bearer {token}"},
                    timeout=10,
                    follow_redirects=True,
                )
            except Exception:
                pass

        STATUS[name] = {"code": code, "time": timestamp}
        status_text = f"{code} {reason}".strip()
        print(f"{timestamp} | {name:<14} | {url:<40} | {status_text}")
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
