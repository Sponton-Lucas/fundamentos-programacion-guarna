# Implementar promedio_aprobados que reciba: alumnos, padrones_habilitados donde 
# alumnos = [[123,8],[456,4],[123,10],[789,7],[123,6]] cada elemento representaL [padron, nota]
# La funcion debe devolver el promedio de las notas aprobadas(>=6) correspondientes a alumnos habilitados.
# Si no existe ningun examen aprobado de alumnos habilitados devolver 0

def promedio_aprobados(alumnos, padrones_habilitados):
    suma_notas = 0
    cantidad_aprobados = 0
    
    for padron, nota in alumnos:
        if padron in padrones_habilitados:
            if nota >= 6:
                suma_notas += nota
                cantidad_aprobados += 1
    
    
    return suma_notas / cantidad_aprobados if cantidad_aprobados > 0 else 0