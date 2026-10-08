# 3) Se cuenta una lista votacion, ya cargada, que contiene sublistas, cada una de esas sublistas tiene los sig valores:
# partido(string), diputados(entero), senadores(entero). Ejemplo:
# [["PP", 19, 35],["PSOE", 20 , 30], ["VOX", 15, 15], ["PP", 0, 15]]. Los recuentos son de diferentes mesas por lo que
# los partidos apareceran varias veces.
# Se pide que escribas un programa en python que procese esa lista y genere un diccionario con clave partido y 
# valor total_votos. El total de votos es la suma de diputados y senadores.
# Luego, debe listar los partidos - total_votos, ordenados de mayor a menor por total_votos.


def procesar_lista(lista):
    dicc = {}

    for partido in lista:
        nombre = partido[0]
        votos = partido[1] + partido[2]

        if nombre in dicc:
            dicc[nombre] += votos
        else:
            dicc[nombre] = votos

    return dicc


def ordenar_imprimir_dicc(dicc):
    dicc_ordenado = sorted(
        dicc.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for clave, valor in dicc_ordenado:
        print(f"Partido: {clave} - Total votos: {valor}")


def main():
    lista = [
        ["PP", 19, 35],
        ["PSOE", 20, 30],
        ["VOX", 15, 15],
        ["PP", 0, 15]
    ]

    dicc = procesar_lista(lista)
    ordenar_imprimir_dicc(dicc)


main()
