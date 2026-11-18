'''
Módulo encargado de validar los datos introducidos por el usuario.
'''
def validar_descripcion(descripcion):
    """Comprueba que la descripción no esté vacía."""

    if not descripcion.strip():
        return False

    return True


def validar_prioridad(prioridad):
    """Comprueba que la prioridad sea válida."""

    # Lista de prioridades permitidas en la aplicación
    prioridades_validas = ["baja", "media", "alta"]

    # Comprobamos que la prioridad introducida exista en la lista
    if prioridad.strip().lower() not in prioridades_validas:
        return False

    return True


def validar_categoria(categoria):
    """Comprueba que la categoría no esté vacía."""

    if not categoria.strip():
        return False

    return True


def validar_id(id_tarea, tareas):
    """Comprueba si existe una tarea con el ID indicado."""

    # No se permiten IDs negativos ni iguales a cero
    if id_tarea <= 0:
        return False

    # Buscamos si existe una tarea con el ID introducido
    for tarea in tareas:

        if tarea["id"] == id_tarea:
            return True

    return False