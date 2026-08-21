import json
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

APP_NAME = "Alive API"
APP_VERSION = "1.5.0"

TOKEN = os.getenv("TOKEN")
KD_HF_TOKEN = os.getenv("KD_HF_TOKEN")
SR_HF_TOKEN = os.getenv("SR_HF_TOKEN")

CORS_ORIGINS_STR = os.getenv("CORS_ORIGINS", '["*"]')
CORS_ORIGINS = json.loads(CORS_ORIGINS_STR)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "*/*",
}

TIMEOUT = 60

DB_DIR = Path(__file__).resolve().parent.parent / "data"
MONITORS_FILE = DB_DIR / "monitors.json"
TEMPLATE_FILE = DB_DIR / "template.json"

MONITORS = json.loads(MONITORS_FILE.read_text(encoding="utf-8")) if MONITORS_FILE.exists() else {}
