from fastapi import Header, HTTPException
from app.config import TOKEN


def verify_token(token: str = Header(..., description="Enter Token")):
    if not TOKEN or token != TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
