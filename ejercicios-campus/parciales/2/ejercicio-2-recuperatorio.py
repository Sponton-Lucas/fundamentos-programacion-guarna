# Escribir una funcion elegir en python para decidir si visitar o no una ciudad.
# Esta funcion debe devolver true si la ciudad se tiene en cuenta en un itinerario,
# False de lo contrario. La funcion recibe dos listas y un entero: una lista de atracciones
# ( atracciones y/o actividades que tiene o se pueden hacer en la ciudad), otra de
# actividades_deseadas(son las actividades que al usuario le gustaria realizar) y un costo
# promedio por actividad.
# La ciudad se aceptara si: Se realizan por lo menos tres actividades deseadas y el costo
# promedio es menor o igual a MAX_COSTO(asumir como predefinida)
# Ejemplos:
# lista_1 = ["museos", "senderismo", "bares", "montañismo"]
# lista_2 = ["bares", "museos", "senderismo", "conciertos"]
# lista_3 = ["bares", "conciertos", "museos"]
# elegir(lista_1, lista_2, 5000) ---> True si 5000 <= MAX_COSTO
# elegir(lista_1, lista_3, 1000) ---> False

def elegir(atraccionesDisponibles, atraccionesDeseadas, valor):
    """Funcion que devuelve True si las actividades deseadas estan disponibles y su valor es menor al costo maximo, o False si no cumple
    MAX_COSTO = 5000
    elegir(["museos", "senderismo", "bares", "montañismo"],["bares", "museos", "senderismo", "conciertos"], 5000))
    True 
    elegir(["museos", "senderismo", "bares", "montañismo"],["bares", "conciertos", "museos"], 1000)
    False
    elegir(["museos", "senderismo", "bares", "montañismo"],["bares", "conciertos", "museos", "senderismo", "baloncesto", "montañismo"], 5500)
    False"""
    MAX_COSTO = 16000
    coincidencias = [actividad for actividad in atraccionesDeseadas if actividad in atraccionesDisponibles]
    return len(coincidencias) >= 3 and valor <= MAX_COSTO
