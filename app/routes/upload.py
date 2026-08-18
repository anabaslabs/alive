import json
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from app.auth import verify_token
from app.services.upload import upload

router = APIRouter()


@router.post("/upload", tags=["Data"], dependencies=[Depends(verify_token)])
async def upload_route(file: UploadFile = File(...)):
    try:
        content = await file.read()
        return upload(content)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file format.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
