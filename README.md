
Proyecto Sprint 8 - Urban Grocers App

Este proyecto automatiza las pruebas del campo name en la creación de kits dentro de la API Urban Grocers.

Proyecto

- configuration.py Contiene la URL base y rutas de la API.
- data.py Contiene los cuerpos de las solicitudes POST.
- sender_stand_request.py Envía las solicitudes a la API.
- create_kit_name_kit_test.py Contiene las pruebas automatizadas.
- .gitignore Excluye archivos innecesarios.
- README.md Descripción del proyecto.

- Cómo ejecutar las pruebas

1. Inicia el servidor en TripleTen.
2. Copia la URL del servidor y actualízala en `configuration.py`.
3. Instala pytest dentro del entorno virtual con: 'python -m pip install pytest'
4. Ejecuta las pruebas con: 'python -m pytest -v'
