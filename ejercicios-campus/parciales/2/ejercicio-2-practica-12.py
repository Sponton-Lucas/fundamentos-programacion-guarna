# Una empresa registra las entregas realizadas por sus repartidores.
# entregas = [(101,15),(205,8),(101,12),(350,20),(205,14),(101,9)]
# repartidores = [(101,"Juan"),(205,"Maria"),(350,"Pedro"),(400,"Ana")]
# Implementar la funcion generar_premios(entregas, repartidores, minimo_km), que devuelva una lista con los nombres
# de los repartidores que hayan realizado al menos una entrega de minimo_km kilometros o mas.
# Para cada repartidor debe aparecer una sola vez en la lista resultado, aun si cumplio la condicion varias veces.


def generar_premios(entregas, repartidores, minimo_km):
    ganadores = []
    for cod_entrega, km in entregas:
        if km >= minimo_km:
            for cod_rep, nombre in repartidores:
                if cod_entrega == cod_rep:
                    if nombre not in ganadores:
                        ganadores.append(nombre)
    return ganadores