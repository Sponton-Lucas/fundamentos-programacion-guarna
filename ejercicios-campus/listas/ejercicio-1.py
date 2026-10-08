#Escribir una función que reciba por parámetro una tupla de números enteros. La
#función deberá devolver 1, si la tupla se encuentra ordenada en forma creciente; -1 si
#la tupla está ordenada en forma decreciente; ó 0 si la tupla está desordenada

def ordenar_tupla(tupla):
    """Funcion que recibe por parametro una tupla de numeros enteros y devuelve 1 si la tupla esta ordenada en forma 
    creciente, -1 si la tupla esta ordenada en forma decreciente, o 0 si la tupla esta desordenada
    >>> ordenar_tupla((1, 2, 3))
    1
    >>> ordenar_tupla((3, 2, 1))
    -1
    >>> ordenar_tupla((1, 3, 2))
    0
    """
    if all(tupla[i] <= tupla[i + 1] for i in range(len(tupla) - 1)):
        return 1
    elif all(tupla[i] >= tupla[i + 1] for i in range(len(tupla) - 1)):
        return -1
    else:
        return 0


