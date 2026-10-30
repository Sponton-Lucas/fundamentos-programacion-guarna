# Una plataforma guarda las notas de distintos alumnos:
# notas = {1001:[8,6,7],1002:[4,5],1003:[10,9,8],1004:[6]}
# Implementar una funcion alumnos_promocionados(notas): que devuelva una lista con los padrones de aquellos alumnos cuyo
# promedio sea mayor o igual a 7.
# Ej: alumnos_promocionados(notas) deberia devolver: [1001,1003]

def alumnos_promocionados(notas):
    aprobados = []
    
    for padron, nota in notas.items():
        suma = 0
        for resultado in nota:
            suma += resultado
        promedio = suma / len(nota)
        if promedio >= 7:
            aprobados.append(padron)
    return aprobados