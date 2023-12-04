import sqlite3
from fastapi import FastAPI, Query, HTTPException
from typing import List

from pydantic import BaseModel

app = FastAPI(title="API de ventas", description="API para consultar ventas", version="1.0.0")

def query_ventas(ciudades: List[str], productos: List[str], total_ventas: str):
    try:
        conn = sqlite3.connect("bbdbventas.db")
        cursor = conn.cursor()

        parametros = []

        if ciudades[0] != "*":
            ciudades = ciudades[0].split(",") 
            condicion_ciudades = "ciudad IN ({})".format(", ".join('?' for _ in ciudades))
            parametros.extend(ciudades)
        else:
            condicion_ciudades = "1=1"

        if productos[0] != "*":
            productos = productos[0].split(",")
            condicion_productos = "producto IN ({})".format(", ".join('?' for _ in productos))
            parametros.extend(productos)
        else:
            condicion_productos = "1=1"

        if total_ventas == "*":
            condicion_total_ventas = "1=1"
        elif total_ventas.startswith(">") or total_ventas.startswith("<"):
            condicion_total_ventas = f"cantidad {total_ventas}"
        else:
            raise ValueError(f"Invalid total_ventas: {total_ventas}")

        query = "SELECT * FROM ventas WHERE {} AND {} AND {}".format(
            condicion_ciudades,
            condicion_productos,
            condicion_total_ventas
        )

        #print(f"Query: {query}")
        result = cursor.execute(query, parametros).fetchall()

        column_names = ["id", "producto", "ciudad", "cantidad"]
        result_dict = [dict(zip(column_names, row)) for row in result]

        return {"response": result_dict}
    except Exception as e:
        raise ValueError(f"Error al procesar ventas: {str(e)}")
    finally:
        # Asegurarse de cerrar la conexión a la base de datos
        if conn:
            conn.close()

@app.get("/ventas/{ciudad}/{producto}/{total_ventas}")
async def recuperar_ventas(ciudad: str, producto: str, total_ventas: str):
    print("ventas_get_parametros_parametros_end_point->") #*
    try:
        # Validar datos y llamar a la función genérica
        ciudad = [ciudad] if ciudad != "*" else ["*"]
        producto = [producto] if producto != "*" else ["*"]
        #print (f"ciudad: {ciudad}, producto: {producto}, total_ventas: {total_ventas}")
        result = query_ventas(ciudad, producto, total_ventas)
        return result
    except Exception as e:
        print(f"Error recuperar ventas/ciudad/producto/total_ventas get:{e}")
        raise HTTPException(status_code=400, detail=f"Invalid query format")

class QueryParams(BaseModel):
        ciudad:str
        producto: str
        total_ventas: str

@app.get("/ventas")
async def recuperar_ventas_get(query: QueryParams):
    print("ventas_get_solicitud_body->") 
    try:
        # Validar datos y llamar a la función genérica
        ciudad = query.ciudad if query.ciudad else ["*"]
        if not isinstance(ciudad, list):
            ciudad = [ciudad]
        producto = query.producto if query.producto else ["*"]
        if not isinstance(producto, list):
            producto = [producto]
        total_ventas = query.total_ventas if query.total_ventas else "*"

        #print(f"ciudad: {ciudad}, producto: {producto}, total_ventas: {total_ventas}")
        result = query_ventas(ciudad, producto, total_ventas)
        return result
    except Exception as e:
        print(f"Error recuperar ventas/ get:{e}")
        raise HTTPException(status_code=400, detail=f"Invalid query format")


@app.get("/ventas)")
async def consultar_ventas_get(ciudad: List[str] = Query(["*"]), 
                               producto: List[str] = Query(["*"]), 
                               total_ventas: str = Query("*")):
    print("ventas_get_parametros_url->") #*
    try:
        # Validar datos y llamar a la función genérica
        #print(f"ciudad: {ciudad}, producto: {producto}, total_ventas: {total_ventas}")
        result = query_ventas(ciudad, producto, total_ventas)
        return result
    except Exception as e:
        print(f"Error consultar ventas/ get:{e}")
        raise HTTPException(status_code=400, detail=f"Invalid query format")

@app.post("/ventas")
async def recuperar_ventas_post(query: dict):
    print("ventas_post->") #*
    try:
        # Validar datos y llamar a la función genérica
        ciudad = query.get("ciudad", ["*"])
        if not isinstance(ciudad, list):
            ciudad = [ciudad]
        producto = query.get("producto", ["*"])
        if not isinstance(producto, list):
            producto = [producto] 
        total_ventas = query.get("total_ventas", "*")
        #print(f"ciudad: {ciudad}, producto: {producto}, total_ventas: {total_ventas}")
        result = query_ventas(ciudad, producto, total_ventas)
        return result
    except Exception as e:
        print(f"Error recuperar ventas/ post:{e}")
        raise HTTPException(status_code=400, detail=f"Invalid query format")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
