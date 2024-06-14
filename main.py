from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from app.frontend.controller.routers import router as frontend_router
from app.api import router as api_router
from app.desing_patterns.creational_patterns.singleton.database_singleton import DatabaseSingleton


__author__ = "Ricardo Robledo"
__version__ = "1.0"


@asynccontextmanager
async def lifespan(app:FastAPI):
    DatabaseSingleton()
    print('startup')
    yield
    print('shutdown')

app = FastAPI(
    title="FastAPI",
    description="API to manage resources in Maestros Joyeros's enterprise",
    version="1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.mount('/static', StaticFiles(directory='app/frontend/frontend_templates/static'), name='static')

app.include_router(frontend_router)
app.include_router(api_router)
