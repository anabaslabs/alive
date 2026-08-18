import json
from app.config import MONITORS_FILE


def update(data: dict) -> dict:
    MONITORS_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return {
        "status": "OK",
        "message": "Updated successfully.",
    }
