# 2) Escribir una funcion elegir en python para decidir asociarse o no a un club. Esta funcion debe devolver
# True is el club es aceptado, False de lo contrario.
# La funcion recibe dos listas y un entero: una de actividades(actividades que se realizan en el club), otra de
# actividades_deseadas(son las actividades que al usuario le gustaria realizar) y un valor de cuota.
# El club se aceptara si:
# Se realizan por lo menos dos actividades deseadas y el valor de la cuota es menor o igual
# a MAX_CUOTA(asumir como predefinida)
# Ejemplos:
lista_1 = ["natacion", "gimnasio", "voley", "futbol"]
lista_2 = ["natacion", "voley", "gimnasio"]
lista_3 = ["natacion", "futbol", "karate"]
# elegir(lista_1,lista_2,5000) ---> True si 5000 <= MAX_CUOTA
# elegir(lista1, lista_3, 5000) ---> True si 5000 <= MAX_CUOTA
# elegir(lista_2, lista_3, 100) ---> False

MAX_CUOTA = 6000
def elegir(actividad, deseada, valorCuota):
    contador_actividades = 0
    for actividades in deseada:
        if actividades in actividad:
            contador_actividades += 1
    
    return (contador_actividades >= 2 and valorCuota <= MAX_CUOTA)

print(elegir(lista_1, lista_2, 5000))
print(elegir(lista_1, lista_3, 5000))
print(elegir(lista_2, lista_3, 100))
print(elegir(lista_2, lista_1, 100))
print(elegir(lista_2, lista_1, 7000))

