import json
import unittest
from fastapi.testclient import TestClient
from app import app  # Asegúrate de reemplazar 'my_module' con el nombre real de tu módulo

class TestVentasAPI(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)
    #recuperar ventas        
    def test_recuperar_ventas_ciudad_producto_total_ventas(self):
        response = self.client.get("/ventas/Madrid/Nissan/>9")
        self.assertEqual(response.status_code, 200)
        # Agrega más aserciones según la estructura de tu respuesta JSON
        # Ejemplo: self.assertEqual(response.json(), {"resultado_esperado": "valor"})

    def test_consultar_ventas_get(self):
        # Prueba con valores válidos
        response = self.client.get("/ventas)?ciudad=Madrid&producto=*&total_ventas=%3E5")
        self.assertEqual(response.status_code, 200)

    #recuperar ventas post
    def test_recuperar_ventas_post(self):
        payload = {
            "ciudad": "*",
            "producto": "Nissan",
            "total_ventas": ">9"
        }
        response = self.client.post("/ventas", json=payload)
        self.assertEqual(response.status_code, 200)
        # Agrega más aserciones según la estructura de tu respuesta JSON
        # Ejemplo: self.assertEqual(response.json(), {"resultado_esperado": "valor"})

if __name__ == '__main__':
   unittest.main()

