#Escribir una función que reciba un valor y calcule el factorial del mismo.
#Si no se puede calcular el factorial del valor recibido, la función deberá devolver 0, de lo contrario deberá devolver el valor calculado.
#No debe imprimir el valor, debe solamente devolverlo.
#La función debe ser testeada, usando el módulo doctest, y se deben incluir al menos 5 casos de prueba que sean significativos.

def calcular_factorial(n):
    """
    Calcula el factorial de un numero entero no negativo n.
    Si n es negativo, devuelve 0.
    >>> calcular_factorial(5)
    120
    >>> calcular_factorial(0)
    1
    >>> calcular_factorial(-1)
    0
    >>> calcular_factorial(3)
    6
    >>> calcular_factorial(1)
    1
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado


print(calcular_factorial(5))  # Debería devolver 120
print(calcular_factorial(0))  # Debería devolver 1
print(calcular_factorial(-1)) # Debería devolver 0
print(calcular_factorial(3))  # Debería devolver 6
print(calcular_factorial(1))  # Debería devolver 1

import doctest
print(doctest.testmod())