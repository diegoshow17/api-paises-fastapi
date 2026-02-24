import requests

BASE_URL = "https://restcountries.com/v3.1"

class PaisNoEncontrado(Exception):
    pass

class ErrorAPIExterna(Exception):
    pass

def obtener_pais(nombre: str):
    response = requests.get(f"{BASE_URL}/name/{nombre}")

    if response.status_code == 404:
        raise PaisNoEncontrado("Pais no encontrado")

    if response.status_code != 200:
        raise ErrorAPIExterna("Error consultando API externa")

    data = response.json()[0]

    return {
        "pais": data["name"]["common"],
        "capital": data["capital"][0] if "capital" in data else "No disponible",
        "poblacion": data["population"],
        "region": data["region"],
        "bandera": data["flags"]["png"]
    }