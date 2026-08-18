import json
from app.config import MONITORS_FILE


def upload(content: bytes) -> dict:
    data = json.loads(content.decode("utf-8"))
    MONITORS_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")

    return {
        "status": "OK",
        "message": "Uploaded successfully.",
    }
