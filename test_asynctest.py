import asynctest
from httpx import Response
from app import recuperar_ventas_get,QueryParams

class TestObtenerVentas(asynctest.TestCase):
    async def test_obtener_ventas(self):
        # Mock httpx.AsyncClient
        mock_client = asynctest.CoroutineMock()
        mock_response = Response(200)
        mock_client.request.return_value.__aenter__.return_value = mock_response

        query = QueryParams(ciudad="*", producto="*", total_ventas=">9")
        with asynctest.patch('httpx.AsyncClient', return_value=mock_client):
            # Llamar a la función
            response = await recuperar_ventas_get(query)

            # Verificar que la respuesta es correcta
            self.assertEqual(mock_response.status_code, 200)

if __name__ == '__main__':
   asynctest.main()

