#Escribir un programa que genere una tupla de 100 valores aleatorios. Cada uno de los
#valores, debe ser entero, y estar entre 0 y 10000, inclusive; y sólo debe aparecer una
#vez. Luego, se deben listar por pantalla los números que sean primos e informar
#cuántos son, y la suma acumulada de los mismos.

import random
import doctest

def validacion_primo(numero):
    """Funcion que recibe por parametro un numero entero y devuelve True si el numero es primo, o False si no lo es
    >>> validacion_primo(2)
    True
    >>> validacion_primo(4)
    False
    >>> validacion_primo(13)
    True
    """
    primo = True
    i = 2
    if numero < 2:
        return False
    while i <= int(numero ** 0.5) and primo:
        if numero % i == 0:
            primo = False
        i += 1
    return primo

def generar_tupla_aleatoria():
    """Funcion que genera una tupla de 100 valores aleatorios entre 0 y 10000, inclusive, sin repetidos
    >>> len(generar_tupla_aleatoria())
    100
    """
    return tuple(random.sample(range(10001), 100))

def main():
    tupla_aleatoria = generar_tupla_aleatoria()
    primos = [num for num in tupla_aleatoria if validacion_primo(num)]
    cantidad_primos = len(primos)
    suma_primos = sum(primos)

    print("Números primos encontrados:", primos)
    print("Cantidad de números primos:", cantidad_primos)
    print("Suma acumulada de los números primos:", suma_primos)

main()

doctest.testmod()