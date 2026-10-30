# Escribir una funcion recomendar_pelicula en python para decidir si una plataforma de streaming es recomendable o no para usarlo.
# La funcion debe devolver True si la plataforma es recomendable y False en caso contrario.
# Recibe dos listas y un entero:
# peliculas_disponibles: lista con las peliculas que tiene la plataforma.
# peliculas_preferidas: lista con las peliculas que le interesan al usuario.
# precio_mensual costo de la suscripcion.
# La plataforma sera recomendada si:
# Tiene al menos 3 peliculas preferidas por el usuario.
# El precio mensual es menor o igual a PRECIO_MAXIMO (suponer constante predefinida)

def recomendar_pelicula(p_disponibles, p_preferidas, precio_mensual):
    contador_peliculas = 0
    
    for peli_p in p_preferidas:
        if peli_p in p_disponibles:
            contador_peliculas += 1

    return (contador_peliculas >= 3 and precio_mensual <= PRECIO_MAXIMO)