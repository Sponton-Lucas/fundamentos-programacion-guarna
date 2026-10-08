# 3) El diccionario sistema_previsional tiene cargados para cada pais (clave) cuatro datos: cantidad de personas trabajando
# cantidad de personas jubiladas, cantidad de personas desempleadas (todos enteros dados en miles) y grupo al que pertenece
# (por ej: "Mercosur", "Union europea", etc)
# Se pide que escribas un programa modular(compuesto por funciones) en python que:
# a) Obtenga el diccionario con los datos haciendo uso de la funcion obtener_datos() que se encuentra en la libreria
# Datos_generales(). La funcion devuelve el diccionario. NO debes escribirla.
# b) Calcule el promedio mundial de personas que estan trabajando, personas jubiladas y personas desempleadas.
# c) Imprima un listado, con los nombres de los paises y su tasa de desempleo, y la relacion jubilados/trabajadores.
# El listado debe estar ordenado de mayor a menor por tasa de desempleo, Indicando :
# Pais - Tasa de desempleo - Relacion jubilados/trabajadores
# d) Genere un nuevo diccionario, donde la clave sea el grupo(por ej, "Mercosur", "Union Europea", etc), los datos asociados
# sean el total de personas que trabajan, el total de jubilados y el total de desempleados.

def calcular_promedio(valor, cantidad):
    return (valor / cantidad)


def mostrar_promedio(diccionario):
    trabajan = 0
    jubilados = 0
    desempleados = 0
    total_paises = len(diccionario)
    for pais in diccionario.items():
        trabajan += pais[1][0]
        jubilados += pais[1][1]
        desempleados += pais[1][2]
    promedio_trabajan = calcular_promedio(trabajan, total_paises)
    promedio_jubilados = calcular_promedio(jubilados, total_paises)
    promedio_desempleados = calcular_promedio(desempleados, total_paises)

def tasa_relacion_pais(diccionario):
    lista = []
    for pais in diccionario.items():
        tasa_desempleo = pais[1][2] / (pais[1][0] + pais[1][2]) * 100
        relacion = pais[1][1] / pais[1][0]
        lista.append([pais[0], tasa_desempleo, relacion])
    lista_ordenada = sorted(lista, key=lambda x: x[1], reverse=True)
    for pais in lista_ordenada:
        print(f"{pais[0]} - {pais[1]:.2f} - {pais[2]:.2f}")

def nuevo_diccionario(diccionario):
    nuevo_dicc = {}
    
    for nombre_pais, datos in diccionario.items():
        grupo = datos[3]
        trabajan = datos[0]
        jubilados = datos[1]
        desempleados = datos[2]
        if grupo not in nuevo_dicc:
            nuevo_dicc[grupo] = [0, 0, 0]
        nuevo_dicc[grupo][0] += trabajan
        nuevo_dicc[grupo][1] += jubilados
        nuevo_dicc[grupo][2] += desempleados
    print(nuevo_dicc)
    return nuevo_dicc

def main():
    #diccionario = obtener_datos()
    sistema_previsional = {
    "Argentina": [22000, 7000, 1800, "Mercosur"],
    "Brasil": [98000, 36000, 8500, "Mercosur"],
    "Uruguay": [1700, 600, 120, "Mercosur"],
    "España": [21000, 9500, 2800, "Union Europea"],
    "Alemania": [45000, 18000, 1500, "Union Europea"]
    }
    mostrar_promedio(sistema_previsional)
    tasa_relacion_pais(sistema_previsional)
    nuevo_diccionario(sistema_previsional)
main()