import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx

app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryParams(BaseModel):
    ciudad: str
    producto: str
    total_ventas: str

@app.post("/obtener_ventas")
async def obtener_ventas(query: QueryParams):
    # Hacer una solicitud GET al servidor FastAPI original
    url = "http://localhost:8000/ventas"
    data = {
        "ciudad": query.ciudad,
        "producto": query.producto,
        "total_ventas": query.total_ventas,
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.request('GET', url, data=json.dumps(data), headers=headers)
            response.raise_for_status()

        # Manejar la respuesta del servidor original
        return JSONResponse(content=response.json())
    except httpx.HTTPError as e:
        # Manejar errores de HTTP
        raise HTTPException(status_code=e.response.status_code, detail=str(e))

    except Exception as e:
        # Manejar otros tipos de excepciones
        raise HTTPException(status_code=500, detail=str(e))
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)