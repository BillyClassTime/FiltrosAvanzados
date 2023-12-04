# Filtros Avanzados en APIRest Python

No hay un estándar  único y universal para la elaboración de solicitudes con filtros avanzados en APIs RESTful. Sin embargo, hay prácticas comunes y convenciones que son seguidas por muchas APIs RESTful para proporcionar una interfaz coherente y fácil de entender.

## Prácticas comunes

A continuación, se describen algunas prácticas comunes relacionadas con la elaboración de solicitudes con filtros en APIs RESTful:

1. **Filtros en la URL (Query Parameters) GET:** Utilizar parámetros de consulta en la URL para especificar los filtros. Esto es común para solicitudes GET. Ejemplo:

   ``` python
   GET /ventas?ciudad=Madrid&producto=Nissan&total_ventas>5
   ```

   Esto filtra las solicitud para todas las ventas de `Nissan`en `Madrid`cuyo total de ventas sea mayor que `5`

2. **Filtros en el Cuerpo de la Solicitud POST:** Para solicitudes que requieren un cuerpo (como POST), los filtros pueden enviarse en el cuerpo de la solicitud en formato JSON u otro formato. Ejemplo:

   ```json
   POST /ventas
   {
       "ciudades": ["Madrid", "Barcelona"],
       "productos": ["Nissan", "Mazda"],
       "total_ventas": ">20"
   }
   ```

   Esto filtra la solicitud por todas las ventas de `Madrid` y `Barcelona`para productos `Nissan`y `Mazda` que su total de ventas sea mayor que `20`

3. **Convenciones de Nomenclatura:** Utilizar convenciones de nomenclatura claras y consistentes para los nombres de los parámetros y valores de filtro. Por ejemplo, utilizar snake_case o camelCase.

4. **Uso de Operadores:** Permitir el uso de operadores en los filtros para expresar condiciones más complejas. Por ejemplo, ">" para valores mayores que, "<" para valores menores que, etc.

5. **Documentación Clara:** Proporcionar una documentación clara que explique cómo construir solicitudes con filtros. Esto incluye ejemplos y descripciones de los parámetros admitidos.

6. **Manejo de Errores:** Implementar un manejo adecuado de errores para informar a los clientes sobre solicitudes incorrectas o mal formadas.
7. **Seguridad:** Considerar la seguridad al permitir el filtrado de datos. Por ejemplo, evitar la inyección de SQL o la exposición de información sensible.
8. **RESTful URI Design:** Diseñar las URI de acuerdo con los principios RESTful, lo que implica el uso de nombres de recursos y acciones verbosas.

> **Nota:** estas prácticas son comunes, pero no hay un estándar único. La elección de cómo diseñar las solicitudes con filtros dependerá de los requisitos específicos de tu API y las preferencias de diseño de tu equipo. Es importante ser coherente y seguir las convenciones de diseño establecidas en tu proyecto o comunidad.



## Prácticas no estandar

Existen algunas prácticas no estandar que tienen ventajas y desventajas pero que no son utilizadas ampliamente por la comunidad.

1. **Solicitudes GET con Diccionario en el body**

   ```Json
   GET /ventas
   {
       "ciudades": ["Madrid", "Barcelona"],
       "productos": ["Nissan", "Mazda"],
       "total_ventas": ">20"
   }
   ```

   #### Ventajas:

   1. **Flexibilidad en los Parámetros:** Al utilizar un diccionario, se permite flexibilidad en los parámetros que un cliente puede incluir en la solicitud. Esto puede ser útil si la API admite una amplia variedad de filtros y se desea permitir a los usuarios enviar cualquier combinación de ellos.
   2. **Sencillez de Implementación:** La implementación es relativamente simple, ya que el diccionario puede contener cualquier clave y valor, lo que hace que la función sea más genérica.

   #### Desventajas:

   1. **Falta de Documentación Explícita:** No hay una documentación explícita sobre los parámetros esperados en la interfaz de la API. Los desarrolladores que consumen la API no tendrán una guía clara sobre qué parámetros pueden enviar y cómo deben estructurarse.

   2. **Menos Validación Explícita:** Al utilizar un diccionario, la validación de los tipos de datos y la existencia de parámetros debe realizarse manualmente en el código, lo que podría llevar a errores si no se maneja correctamente.

   3. **Complejidad en la Lógica de Negocio:** La lógica de procesamiento de la solicitud dentro de la función se complica debido a la necesidad de validar y transformar los datos del diccionario antes de pasarlos a la función de consulta.

   4. **Menor Claridad en la Documentación Automática:** Las herramientas de generación automática de documentación pueden tener dificultades para entender y presentar de manera clara los detalles de la interfaz de la API cuando se utilizan diccionarios para pasar parámetros.

   5. **No soportado por algunos clientes APIRestful**: Alguno frameworks como `FastAPI` soportan la creación de solicitudes `GET` con cuerpo en el mensaje, pero algunos clientes como clientes `httpx`e incluso el cliente `FastAPI`no soportan estas solicitudes.

      Nota: Se incluye en este escenario un cliente `front-end.py` que llama a la `API Rest` con el método `GET`y un cuerpo de solicitudes, pero la ruta de solicitud hacia posibles paginas renderizadas son `POST`.

2. **Parámetros directamente en la ruta**

   Si la variedad de parámetros es extensa, los parámetros de consulta (query parameters) en la URL suelen ser preferidos para mejorar la claridad y la documentación.

   ```
   GET /ventas/*/Nissan/>9
   ```

   #### Ventajas

   1. **Claridad y Legibilidad**: Al incluir los parámetros directamente en la URL, la solicitud se vuelve más clara y legible. Los usuarios de la API pueden entender fácilmente la intención de la solicitud al ver los parámetros en la URL.

   2. **Documentación Explícita**: Los parámetros en la URL son fácilmente documentados y comprendidos. La información sobre los parámetros puede ser incluida directamente en la documentación de la API, facilitando a los desarrolladores entender cómo interactuar con la API.

   3. **Facilita la Navegación**: Los parámetros en la URL permiten a los usuarios copiar y pegar la URL para repetir la misma consulta, facilitando la navegación y el uso de la API.

   #### Desventajas

   1. **Limitación de Longitud de URL:** Algunos navegadores y servidores pueden tener restricciones en la longitud de las URL. Si la combinación de parámetros es demasiado extensa, podría generar problemas en algunos entornos.
   2. **Menos Seguridad para Datos Sensibles:** Los parámetros en la URL son visibles en la barra de direcciones y en los registros del servidor, lo que podría ser un problema si los parámetros contienen información sensible.

## Conclusiones

- La elección entre estos métodos depende de la naturaleza de la operación y la complejidad de los filtros.
- Para operaciones simples y comunes, los filtros en la URL (Query Parameters) son preferidos.
- Los filtros en el cuerpo de la solicitud (POST) son ideales para filtros complejos y grandes conjuntos de datos.
- La claridad, la legibilidad y la documentación explícita son factores clave para una buena práctica en el diseño de APIs RESTful.

| Método de Filtro                                 | Ventajas                                                     | Desventajas                                                  | Recomendaciones                                              |
| ------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Filtros en la URL (Query Parameters)**         | - Claridad y legibilidad en la URL. - Facilidad de documentación explícita. - Fácil repetición y navegación. | - Posibles limitaciones de longitud de URL. - Visibilidad de parámetros en registros y en la barra de direcciones. | - Adecuado para filtros simples y comunes en operaciones de consulta. |
| **Filtros en el Cuerpo de la Solicitud (POST)**  | - Permite envío de datos más complejos. - Puede manejar grandes conjuntos de datos sin restricciones de URL. - Datos sensibles no son visibles en la URL. | - Menos legible en términos de URL. - Requiere un cuerpo de solicitud, lo que podría no ser adecuado para todas las operaciones. | - Adecuado para operaciones que involucran filtros complejos o grandes conjuntos de datos. |
| **Solicitudes GET con Diccionario en el Cuerpo** | - Flexibilidad en los parámetros permitidos. - Implementación relativamente simple. | - Falta de documentación explícita sobre los parámetros. - Menos validación explícita. - Complejidad en la lógica de procesamiento. | - Menos común en prácticas de API RESTful debido a la falta de claridad y documentación.<br />- No soportado por algunos clientes de **APIRest**. |
| **Parámetros Directamente en la Ruta (GET)**     | - Muy claro y legible en la URL. - Documentación explícita y fácil comprensión. | - Limitado en la cantidad de parámetros que se pueden incluir. | - Adecuado para operaciones de consulta con un número limitado de parámetros. |