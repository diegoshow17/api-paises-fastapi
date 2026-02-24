from fastapi import HTTPException
from app.services.pais_service import (
    obtener_pais,
    PaisNoEncontrado,
    ErrorAPIExterna
)

def get_pais(nombre: str):
    try:
        return obtener_pais(nombre)
    except PaisNoEncontrado as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ErrorAPIExterna:
        raise HTTPException(status_code=500, detail="Error consultando la API externa")