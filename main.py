"""
Módulo principal del gestor de tareas.
Controla el flujo de ejecución de la aplicación.
"""

from data_handler import (
    cargar_tareas,
    crear_tarea,
    listar_tareas,
    editar_tarea,
    eliminar_tarea,
    cambiar_estado_tarea,
    buscar_tareas,
    filtrar_por_categoria
)

from utils import (
    validar_descripcion,
    validar_prioridad,
    validar_categoria,
    validar_id
)

from reports import (
    contar_pendientes,
    contar_completadas,
    contar_por_prioridad,
    porcentaje_estado
)


def mostrar_menu():
    """Muestra las opciones principales de la aplicación."""

    print("\n========== GESTOR DE TAREAS ==========")
    print("1. Crear tarea")
    print("2. Listar tareas")
    print("3. Editar tarea")
    print("4. Eliminar tarea")
    print("5. Cambiar estado de una tarea")
    print("6. Buscar tareas por palabra clave")
    print("7. Filtrar tareas por categoría")
    print("8. Mostrar estadísticas")
    print("0. Salir")
    print("======================================")


def main():
    """Controla el flujo principal de la aplicación."""

    # Cargamos las tareas guardadas en el archivo JSON
    tareas = cargar_tareas()

    # Si ocurre algún problema al cargar los datos,
    # se muestra un mensaje y se cierra el programa
    if tareas is None:
        print("No se puede iniciar la aplicación. Revisa el archivo tareas.json.")
        return

    # Bucle principal de la aplicación
    while True:

        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

        except ValueError:
            print("Error: debe introducir un número válido.")
            continue

        match opcion:

            # Opción para crear una nueva tarea
            case 1:

                descripcion = input("Introduce la descripción: ")

                # Comprobamos que la descripción no esté vacía
                if not validar_descripcion(descripcion):
                    print("Error: la descripción no puede estar vacía.")
                    continue

                prioridad = input("Introduce la prioridad (baja, media, alta): ")

                # Validamos que la prioridad introducida sea correcta
                if not validar_prioridad(prioridad):
                    print("Error: la prioridad no es válida.")
                    continue

                categoria = input("Introduce la categoría: ")

                # Comprobamos que la categoría tenga contenido
                if not validar_categoria(categoria):
                    print("Error: la categoría no puede estar vacía.")
                    continue

                # Creamos la tarea usando los datos introducidos por el usuario
                resultado = crear_tarea(
                    tareas,
                    descripcion.strip(),
                    prioridad.strip().lower(),
                    categoria.strip()
                )
                if resultado is not None:
                    print("Tarea creada correctamente.")
                else:
                    print("No se ha podido crear la tarea")

            # 2. Listar tareas
            case 2:

                listar_tareas(tareas)

            # 3. Editar tarea
            case 3:

                if not tareas:
                    print("No hay tareas para modificar.")
                    continue

                # Mostramos las tareas para que el usuario pueda escoger una
                listar_tareas(tareas)

                try:
                    id_tarea = int(input("Introduce el ID de la tarea: "))

                except ValueError:
                    print("Error: debes introducir un número entero.")
                    continue

                # Verificamos que el ID exista dentro de la lista de tareas
                if not validar_id(id_tarea, tareas):
                    print("Error: el ID introducido no existe.")
                    continue

                # Buscar la tarea seleccionada por el usuario
                tarea_actual = {}

                for tarea in tareas:
                    if tarea["id"] == id_tarea:
                        tarea_actual = tarea

                print(f"\nDeja el campo vacío que no quieres modificar de la tarea con ID {id_tarea}.")

                print(f"Descripción actual ({tarea_actual['descripcion']})")
                nueva_descripcion = input("Introduce la nueva descripción: ")

                print(f"Prioridad actual ({tarea_actual['prioridad']})")
                nueva_prioridad = input("Introduce la nueva prioridad: ")

                print(f"Categoría actual ({tarea_actual['categoria']})")
                nueva_categoria = input("Introduce la nueva categoría : ")

                # Si el usuario deja algún campo vacío,
                # se conserva el valor anterior
                if not nueva_descripcion.strip():
                    nueva_descripcion = tarea_actual["descripcion"]

                if not nueva_prioridad.strip():
                    nueva_prioridad = tarea_actual["prioridad"]

                if not nueva_categoria.strip():
                    nueva_categoria = tarea_actual["categoria"]

                # Validamos los nuevos datos
                if not validar_descripcion(nueva_descripcion):
                    print("Error: la descripción no puede estar vacía.")
                    continue

                if not validar_prioridad(nueva_prioridad):
                    print("Error: la prioridad no es válida.")
                    continue

                if not validar_categoria(nueva_categoria):
                    print("Error: la categoría no puede estar vacía.")
                    continue

                resultado = editar_tarea(
                    tareas,
                    id_tarea,
                    nueva_descripcion.strip(),
                    nueva_prioridad.strip().lower(),
                    nueva_categoria.strip()
                )

                if resultado:
                    print("Tarea modificada correctamente.")
                else:
                    print("No se ha podido modificar la tarea.")

            # 4. Eliminar tarea
            case 4:

                if not tareas:
                    print("No hay tareas para eliminar.")
                    continue

                listar_tareas(tareas)

                try:
                    id_tarea = int(input("Introduce el ID de la tarea: "))

                except ValueError:
                    print("Error: debes introducir un número entero.")
                    continue

                if not validar_id(id_tarea, tareas):
                    print("Error: el ID introducido no existe.")
                    continue

                resultado = eliminar_tarea(tareas, id_tarea)

                if resultado:
                    print("Tarea eliminada correctamente.")
                else:
                    print("No se ha podido eliminar la tarea.")

            # 5. Cambiar estado de la tarea
            case 5:

                if not tareas:
                    print("No hay tareas registradas.")
                    continue

                listar_tareas(tareas)

                try:
                    id_tarea = int(input("Introduce el ID de la tarea: "))

                except ValueError:
                    print("Error: debes introducir un número entero.")
                    continue

                if not validar_id(id_tarea, tareas):
                    print("Error: el ID introducido no existe.")
                    continue

                # Buscar la tarea seleccionada por el usuario
                tarea_actual = {}

                for tarea in tareas:
                    if tarea["id"] == id_tarea:
                        tarea_actual = tarea

                # Comprobamos si la tarea está pendiente o completada
                if not tarea_actual["completada"]:

                    print("La tarea está pendiente.")
                    respuesta = input("¿Quieres marcarla como completada? (s/n): ")

                    if respuesta.strip().lower() == "s":
                        resultado = cambiar_estado_tarea(tareas, id_tarea)

                        if resultado:
                            print("La tarea se ha marcado como completada.")

                        else:
                            print("No se ha podido guardar el cambio")

                    elif respuesta.strip().lower() == "n":
                        print("No se ha modificado el estado.")

                    else:
                        print("Respuesta no válida.")

                else:

                    print("La tarea está completada.")
                    respuesta = input("¿Quieres marcarla como pendiente? (s/n): ")

                    if respuesta.strip().lower() == "s":

                        # Cambiamos el estado de la tarea
                        resultado = cambiar_estado_tarea(tareas, id_tarea)

                        if resultado:
                            print("La tarea se ha marcado como pendiente.")

                        else:
                            print("No se ha podido guardar el cambio")

                    elif respuesta.strip().lower() == "n":
                        print("No se ha modificado el estado.")

                    else:
                        print("Respuesta no válida.")

            # 6. Buscar tareas por palabra clave
            case 6:

                if not tareas:
                    print("No hay tareas registradas.")
                    continue

                # Pedimos una palabra para buscar coincidencias
                palabra = input("Introduce la palabra que quieres buscar: ")

                if not palabra.strip():
                    print("Error: debes introducir una palabra.")
                    continue

                # Se obtienen todas las tareas que contienen la palabra indicada
                tareas_encontradas = buscar_tareas(tareas, palabra.strip())

                print("\n========== RESULTADOS DE BÚSQUEDA ==========")

                listar_tareas(tareas_encontradas)

            # 7. Filtrar por categoría
            case 7:

                if not tareas:
                    print("No hay tareas registradas.")
                    continue

                categoria = input("Introduce la categoría que quieres consultar: ")

                if not validar_categoria(categoria):
                    print("Error: la categoría no puede estar vacía.")
                    continue

                # Permite mostrar únicamente las tareas
                # que pertenecen a una categoría concreta
                tareas_encontradas = filtrar_por_categoria(tareas, categoria.strip())

                print("\n========== TAREAS POR CATEGORÍA ==========")

                listar_tareas(tareas_encontradas)

            # 8. Mostrar estadísticas
            case 8:

                # Calculamos diferentes estadísticas sobre las tareas
                pendientes = contar_pendientes(tareas)
                completadas = contar_completadas(tareas)

                # Obtenemos los porcentajes según estado y prioridad
                porcentajes_estado = porcentaje_estado(tareas)
                porcentajes_prioridad = contar_por_prioridad(tareas)

                print("\n========== ESTADÍSTICAS ==========")

                print(f"Total de tareas: {len(tareas)}")

                print("\nEstado de las tareas:")
                print(f"Tareas pendientes: {pendientes}")
                print(f"Tareas completadas: {completadas}")

                print("\nPorcentaje según estado:")
                print(f"Pendientes: {porcentajes_estado['pendientes']:.2f}%")
                print(f"Completadas: {porcentajes_estado['completadas']:.2f}%")

                print("\nDistribución por prioridad:")
                print(f"Prioridad baja: {porcentajes_prioridad['baja']:.2f}%")
                print(f"Prioridad media: {porcentajes_prioridad['media']:.2f}%")
                print(f"Prioridad alta: {porcentajes_prioridad['alta']:.2f}%")

                print("==================================")

            # 0. Salir
            case 0:
                print("Gracias por utilizar el gestor de tareas.")
                print("¡Hasta pronto!")
                break

            # Opción no válida
            case _:
                print("Error: selecciona una opción del menú.")


# Este bloque asegura que la función principal
# solo se ejecute cuando se inicia este archivo directamente
if __name__ == "__main__":
    main()