from fastapi import APIRouter, Body, Depends
from pydantic import BaseModel
from app.config import MONITORS
from app.auth import verify_token
from app.services.update import update

router = APIRouter()


class MonitorItem(BaseModel):
    url: str
    interval: int


SWAGGER_EXAMPLE = {"Current Config": {"value": MONITORS}}


@router.put("/update", tags=["Data"], dependencies=[Depends(verify_token)])
async def update_route(data: dict[str, MonitorItem] = Body(openapi_examples=SWAGGER_EXAMPLE)):
    return update({name: item.model_dump() for name, item in data.items()})
