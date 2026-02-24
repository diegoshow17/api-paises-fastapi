from fastapi import APIRouter
from app.controllers.pais_controller import get_pais

router = APIRouter()

@router.get("/paises/{nombre}")
def obtener_pais(nombre: str):
    return get_pais(nombre)