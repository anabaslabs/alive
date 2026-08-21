import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

from app.config import APP_NAME, APP_VERSION, CORS_ORIGINS, MONITORS
from app.routes.delete import router as delete_router
from app.routes.download import router as download_router
from app.routes.monitor import router as monitor_router
from app.routes.update import router as update_router
from app.routes.upload import router as upload_router
from app.services.monitor import monitor


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with httpx.AsyncClient() as client:
        tasks = [
            asyncio.create_task(monitor(name, data["url"], data["interval"], client))
            for name, data in MONITORS.items()
        ]
        yield
        for t in tasks:
            t.cancel()


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Health"])
async def root():
    return {
        "name": APP_NAME,
        "version": APP_VERSION,
        "status": "OK",
        "swagger-ui": "https://alive.anabaslabs.com/docs"
    }


app.include_router(monitor_router)
app.include_router(download_router)
app.include_router(upload_router)
app.include_router(update_router)
app.include_router(delete_router)
