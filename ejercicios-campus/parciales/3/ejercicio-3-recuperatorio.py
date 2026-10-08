#En el programa “Camino a la fama”, los participantes muestran sus aptitudes: baile, canto, etc.
#Un jurado vota a los participantes colocando un puntaje del 1 al 10. 
#Esto genera una lista de listas (cada sublista es una votación). 
#Ejemplo: [ [“Luisa”, 4], [“Mariano”, 10], [“Luisa”, 5], etc…].
#Las votaciones son de distintos jueces y por distintas actuaciones por lo que los participantes aparecerán varias veces.
#Se pide que escribas un programa en Python que procese esa lista y genere un diccionario con clave participante y valores:
# sumatoria_puntaje, cantidad_puntajes, promedio_puntaje.  
#Luego, debe listar: participantes – promedio_puntaje, ordenados de mayor a menor por promedio_puntaje. 
# Con el ejemplo anterior debería quedar:
#Mariano	10
#Luisa		4.5

def procesarLista(lista):
    puntuacion = {}
    for participante in lista:
        if participante[0] not in puntuacion:
            puntuacion[participante[0]] = [participante[1], 1]
        else:
            puntuacion[participante[0]][0] += participante[1]
            puntuacion[participante[0]][1] += 1
    for participante in puntuacion:
        sumatoria = puntuacion[participante][0]
        cantidad = puntuacion[participante][1]
        promedio = sumatoria / cantidad
        puntuacion[participante].append(promedio)
    return puntuacion

def listarPromedios(puntuacion):
    promedios = []
    for participante in puntuacion:
        promedios.append((participante, puntuacion[participante][2]))
    
    promedios.sort(key=lambda x: x[1], reverse=True)
    
    for participante, promedio in promedios:
        print(f"{participante}\t{promedio:.1f}")

def main():
    lista_votaciones = [
        ["Luisa", 4],
        ["Mariano", 10],
        ["Luisa", 5],
        ["Carlos", 7],
        ["Mariano", 8],
        ["Carlos", 9]
    ]
    puntuacion = procesarLista(lista_votaciones)
    listarPromedios(puntuacion)

if __name__ == "__main__":
    main()
