from fastapi import APIRouter, Depends
from app.auth import verify_token
from app.services.delete import delete

router = APIRouter()


@router.delete("/delete", tags=["Data"], dependencies=[Depends(verify_token)])
async def delete_route():
    return delete()
