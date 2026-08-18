from fastapi import APIRouter, Body
from pydantic import BaseModel
from app.config import MONITORS
from app.services.update import update

router = APIRouter()


class MonitorItem(BaseModel):
    url: str
    interval: int


SWAGGER_EXAMPLE = {"Current Config": {"value": MONITORS}}


@router.put("/update", tags=["Database"])
async def update_route(data: dict[str, MonitorItem] = Body(openapi_examples=SWAGGER_EXAMPLE)):
    return update({name: item.model_dump() for name, item in data.items()})
