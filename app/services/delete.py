from app.config import MONITORS_FILE


def delete() -> dict:
    if MONITORS_FILE.exists():
        MONITORS_FILE.unlink()

    return {
        "status": "OK",
        "message": "Deleted successfully.",
    }
