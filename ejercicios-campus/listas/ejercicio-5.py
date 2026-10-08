#Escribir una función que indique si los 5 dados que han sido arrojados por un jugador,
#forman escalera. La función recibirá por parámetro, una tupla, con los 5 valores
#obtenidos al arrojar los dados. Deberá devolver True, si forman escalera, de lo
#contrario, deberá devolver, False.
#Para que se de escalera, hay 3 alternativas: (1,2,3,4,5); (2,3,4,5,6) ó (3,4,5,6,1),
#claro que el orden en el que aparecen los valores, no importa
import doctest
def es_escalera(dados):
    """Funcion que determina si los 5 dados forman una escalera
    >>> es_escalera((1,2,3,4,5))
    True
    >>> es_escalera((2,3,4,5,6))
    True
    >>> es_escalera((3,4,5,6,1))
    True
    >>> es_escalera((1,2,3,4,6))
    False
    """
    dados_ordenados = sorted(dados)
    if dados_ordenados == [1, 2, 3, 4, 5] or dados_ordenados == [2, 3, 4, 5, 6] or dados_ordenados == [1, 3, 4, 5, 6]:
        return True
    return False

print(es_escalera((1, 2, 3, 4, 5)))  # True
print(es_escalera((2, 3, 4, 5, 6)))  # True
print(es_escalera((3, 4, 5, 6, 1)))  # True
print(es_escalera((1, 2, 3, 4, 6)))  # False
print(es_escalera((1, 3, 4, 5, 6)))  # True
print(es_escalera((5, 2, 3, 4, 1)))  # True

doctest.testmod()