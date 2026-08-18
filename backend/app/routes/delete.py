from fastapi import APIRouter
from app.services.delete import delete

router = APIRouter()


@router.delete("/delete", tags=["Database"])
async def delete_route():
    return delete()
