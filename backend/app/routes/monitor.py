from fastapi import APIRouter
from app.services.monitor import status

router = APIRouter()


@router.post("/monitor", tags=["Alive"])
async def monitor_route():
    return status()
