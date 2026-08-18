import json
from fastapi import APIRouter, File, HTTPException, UploadFile
from app.services.upload import upload

router = APIRouter()


@router.post("/upload", tags=["Database"])
async def upload_route(file: UploadFile = File(...)):
    try:
        content = await file.read()
        return upload(content)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file format.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
