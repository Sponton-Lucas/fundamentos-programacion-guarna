# alumnos = [[123,8],[456,4],[123,10],[789,7],[123,6]] cada elemento es [padron, nota]
# Implementar contar_aprobados(alumnos, padrones_habilitados) que devuelva cuantos examenes aprobados
#(nota >= 6) pertenecen a alumnos habilitados

def contar_aprobados(alumnos, padrones_habilitados):
    cantidad_aprobados = 0
    
    for padron, nota in alumnos:
        if padron in padrones_habilitados:
            if nota >= 6:
                cantidad_aprobados += 1
    return cantidad_aprobados