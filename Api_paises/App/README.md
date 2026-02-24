📌 Descripción General

Esta API permite consultar información básica de países como nombre, capital, población, región y bandera.

La API consume datos desde la API pública REST Countries y devuelve una respuesta estructurada y simplificada.

📌 Endpoint Implementado
GET /api/paises/{nombre}

Consulta información de un país por nombre.

Parámetros

nombre (string): Nombre del país

Ejemplo de petición
GET http://127.0.0.1:8000/api/paises/colombia
📌 Respuesta Exitosa (200)
{
  "pais": "Colombia",
  "capital": "Bogotá",
  "poblacion": 50882884,
  "region": "Americas",
  "bandera": "https://flagcdn.com/w320/co.png"
}

📌 Manejo de Errores
404 – País no encontrado
{
  "detail": "Pais no encontrado"
}
500 – Error consultando API externa
{
  "detail": "Error consultando la API externa"
}
📌 Tecnologías utilizadas

Python

FastAPI

Requests

Uvicorn

📌 Cómo ejecutar el proyecto
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload