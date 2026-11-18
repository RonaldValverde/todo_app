"""
Módulo encargado de gestionar las tareas de la aplicación.
"""
import json


def cargar_tareas(ruta="tareas.json"):
    """Carga las tareas almacenadas en el archivo JSON."""

    # Intentamos abrir y leer el archivo JSON
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            tareas = json.load(archivo)

        return tareas

    except FileNotFoundError:
        print(f"El archivo '{ruta}' no existe. Se iniciará una lista vacía.")
        return []

    except json.JSONDecodeError as e:
        print(f"Error: El archivo contiene un JSON mal formado en la línea {e.lineno}.")
        return None

    except OSError as e:
        print(f"Error al leer el archivo: {e}")
        return None


def guardar_tareas(tareas, ruta="tareas.json"):
    """Guarda las tareas en el archivo JSON."""

    if tareas is None:
        print("No se pueden guardar las tareas porque no se han podido cargar.")
        return False

    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(tareas, archivo, indent=4, ensure_ascii=False)

        return True

    except OSError as e:
        print(f"Error al guardar el archivo: {e}")
        return False


def crear_tarea(tareas, descripcion, prioridad, categoria):
    """Crea una tarea nueva y la guarda en el archivo JSON."""

    if tareas is None:
        print("No se puede crear la tarea porque no se han podido cargar los datos.")
        return None

    # Si ya existen tareas, el nuevo ID será el siguiente disponible
    if tareas:
        nuevo_id = max(tarea["id"] for tarea in tareas) + 1
    else:
        nuevo_id = 1

    nueva_tarea = {
        "id": nuevo_id,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "completada": False,
        "categoria": categoria
    }

    # Añadimos la nueva tarea a la lista
    tareas.append(nueva_tarea)

    # Guardamos los cambios en el archivo JSON
    if guardar_tareas(tareas):
        return tareas

    tareas.remove(nueva_tarea)
    return None


def listar_tareas(tareas):
    """Muestra todas las tareas almacenadas."""

    if not tareas:
        print("No hay tareas registradas.")
        return

    print("\n=========== LISTA DE TAREAS ===========")

    for tarea in tareas:

        # Mostramos "Completada" o "Pendiente" según el estado de la tarea
        if tarea["completada"]:
            estado = "Completada"
        else:
            estado = "Pendiente"

        print(f"\nID: {tarea['id']}")
        print(f"Descripción: {tarea['descripcion']}")
        print(f"Prioridad: {tarea['prioridad']}")
        print(f"Estado: {estado}")
        print(f"Categoría: {tarea['categoria']}")
        print("-------------------------------------")

    print("\n======== FIN LISTA DE TAREAS =========")


def editar_tarea(tareas, id_tarea, nueva_descripcion, nueva_prioridad, nueva_categoria):
    """Modifica los datos de una tarea existente."""

    for tarea in tareas:

        if tarea["id"] == id_tarea:

            descripcion_anterior = tarea["descripcion"]
            prioridad_anterior = tarea["prioridad"]
            categoria_anterior = tarea["categoria"]

            tarea["descripcion"] = nueva_descripcion
            tarea["prioridad"] = nueva_prioridad
            tarea["categoria"] = nueva_categoria

            if guardar_tareas(tareas):
                return True

            tarea["descripcion"] = descripcion_anterior
            tarea["prioridad"] = prioridad_anterior
            tarea["categoria"] = categoria_anterior

            return False

    return False


def eliminar_tarea(tareas, id_tarea):
    """Elimina una tarea y reorganiza los identificadores."""

    for tarea in tareas:

        if tarea["id"] == id_tarea:

            tareas_originales = [t.copy() for t in tareas]

            tareas.remove(tarea)

            # Reorganizamos los IDs para que no queden huecos tras eliminar una tarea
            for i, tarea in enumerate(tareas, start=1):
                tarea["id"] = i

            if guardar_tareas(tareas):
                return True

            tareas[:] = tareas_originales
            return False

    return False


def cambiar_estado_tarea(tareas, id_tarea):
    """Cambia el estado de una tarea entre pendiente y completada."""

    for tarea in tareas:

        if tarea["id"] == id_tarea:

            estado_anterior = tarea["completada"]
            # Cambia el estado actual por el contrario:
            # pendiente -> completada o completada -> pendiente
            tarea["completada"] = not tarea["completada"]

            if guardar_tareas(tareas):
                return True

            tarea["completada"] = estado_anterior
            return False

    return False


def buscar_tareas(tareas, palabra):
    """Busca tareas que contengan una palabra en su descripción."""

    tareas_encontradas = []

    for tarea in tareas:

        # Busca coincidencias ignorando mayúsculas y minúsculas
        if palabra.lower() in tarea["descripcion"].lower():
            tareas_encontradas.append(tarea)

    return tareas_encontradas


def filtrar_por_categoria(tareas, categoria):
    """Filtra las tareas según la categoría indicada."""

    tareas_encontradas = []

    for tarea in tareas:

        if tarea["categoria"].strip().lower() == categoria.strip().lower():
            tareas_encontradas.append(tarea)

    return tareas_encontradas
