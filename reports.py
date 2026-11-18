"""
Módulo de estadísticas del gestor de tareas.
"""

def contar_pendientes(tareas):
    """Cuenta el número de tareas pendientes."""

    # Variable que almacenará el número de tareas pendientes
    contador = 0

    # Recorremos todas las tareas
    for tarea in tareas:
        # Si la tarea no está completada, aumentamos el contador
        if not tarea["completada"] :
            contador += 1

    return contador


def contar_completadas(tareas):
    """Cuenta el número de tareas completadas."""

    # Variable para contar las tareas completadas
    contador = 0

    # Recorremos la lista de tareas
    for tarea in tareas:
        # Sumamos 1 cuando la tarea está completada
        if tarea["completada"] :
            contador += 1

    return contador


def porcentaje_estado(tareas):
    """Calcula el porcentaje de tareas pendientes y completadas."""

    # Obtenemos el número total de tareas
    total_tareas = len(tareas)

    # Evitamos una división entre cero si no existen tareas
    if total_tareas == 0:
        return {
            "pendientes": 0,
            "completadas": 0
        }

    # Obtenemos el número de tareas pendientes y completadas
    pendientes = contar_pendientes(tareas)
    completadas = contar_completadas(tareas)

    # Calculamos los porcentajes respecto al total
    porcentaje_pendientes = (pendientes / total_tareas) * 100
    porcentaje_completadas = (completadas / total_tareas) * 100

    return {
        "pendientes": porcentaje_pendientes,
        "completadas": porcentaje_completadas
    }


def contar_por_prioridad(tareas):
    """Calcula el porcentaje de tareas según su prioridad."""

    # Calculamos el número total de tareas
    total_tareas = len(tareas)

    # Si no hay tareas, devolvemos 0 en todas las prioridades
    if total_tareas == 0:
        return {
            "baja": 0,
            "media": 0,
            "alta": 0
        }

    # Diccionario para contar cuántas tareas hay de cada prioridad
    contador = {
        "baja": 0,
        "media": 0,
        "alta": 0
    }

    # Recorremos todas las tareas
    for tarea in tareas:

        # Guardamos la prioridad en minúsculas para evitar errores
        prioridad = tarea["prioridad"].lower()

        # Incrementamos el contador de la prioridad correspondiente
        if prioridad in contador:
            contador[prioridad] += 1

    # Diccionario donde se almacenarán los porcentajes
    porcentajes = {}

    # Calculamos el porcentaje de cada prioridad
    for prioridad, cantidad in contador.items():
        porcentajes[prioridad] = (cantidad / total_tareas) * 100

    return porcentajes
