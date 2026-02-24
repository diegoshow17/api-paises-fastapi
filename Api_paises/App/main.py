from fastapi import FastAPI
from app.routes.paises import router as pais_router

app = FastAPI(title="API de Paises")

app.include_router(pais_router, prefix="/api")