# Gestor de tareas - Todo List

## ¿En qué consiste este proyecto?

Este proyecto es una aplicación de gestión de tareas que he desarrollado con Python como parte de mi aprendizaje.

La idea es crear un programa sencillo que permita organizar las tareas del día a día, consultar cuáles están pendientes y cuáles se han completado.

Las tareas se guardan en un archivo JSON para que no se pierdan cuando se cierra el programa.

## ¿Qué se puede hacer con la aplicación?

Con este programa se pueden realizar las siguientes acciones:

- Crear nuevas tareas.
- Ver todas las tareas guardadas.
- Modificar una tarea cuando sea necesario.
- Eliminar tareas.
- Marcar tareas como completadas o pendientes.
- Buscar tareas por una palabra.
- Consultar las tareas según su categoría.
- Ver estadísticas sobre las tareas, como cuántas están pendientes, completadas o qué prioridad tienen.

Cada tarea tiene una descripción, una prioridad, una categoría y un estado.

## ¿Qué he utilizado?

Para desarrollar este proyecto he utilizado:

- **Python:** para crear el programa y sus diferentes funciones.
- **JSON:** para guardar las tareas y poder recuperarlas al volver a abrir la aplicación.
- **PyCharm:** como entorno para escribir y probar el código.
- **Git:** para llevar un seguimiento de los cambios realizados en el proyecto.

## Organización de los archivos

El proyecto está dividido en varios archivos para tener el código mejor organizado:

```text
todo_app/
|
|-- main.py
|-- data_handler.py
|-- reports.py
|-- utils.py
|-- tareas.json
|-- README.md
```



Cada archivo tiene una función:

- **main.py:** es el archivo principal. Desde aquí se muestra el menú y se controla el funcionamiento del programa.
- **data_handler.py:** contiene las funciones para crear, mostrar, modificar, eliminar y guardar las tareas.
- **reports.py:** se encarga de calcular las estadísticas.
- **utils.py:** contiene las funciones que comprueban que los datos introducidos sean correctos.
- **tareas.json:** es el archivo donde se guardan las tareas.
- **README.md:** contiene información sobre el proyecto.

## ¿Cómo ejecutar el programa?

Para utilizar la aplicación es necesario tener Python instalado.

Una vez abierta la carpeta del proyecto en PyCharm, se puede ejecutar desde la terminal con el siguiente comando:

```bash
python main.py
```

Cuando se inicie el programa aparecerá un menú con las diferentes opciones. Solo hay que introducir el número de la opción que se quiera utilizar.

## Lo que he aprendido con este proyecto

Con el desarrollo de esta aplicación he podido practicar diferentes conceptos de Python, como el uso de funciones, listas, diccionarios, condiciones, bucles, validaciones y gestión de errores.

También he aprendido a separar el código en diferentes archivos y a trabajar con archivos JSON para guardar información.

Ha sido una práctica que me ha permitido aplicar lo aprendido y mejorar poco a poco mis conocimientos de programación.