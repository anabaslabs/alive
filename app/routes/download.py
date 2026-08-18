from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.services.download import download

router = APIRouter()


@router.get("/download", tags=["Data"])
async def download_route():
    return FileResponse(
        path=download(),
        filename="template.json",
        media_type="application/json",
    )
