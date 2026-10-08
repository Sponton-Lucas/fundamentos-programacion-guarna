# Reescriba el código que está debajo, para que la función sólo devuelva true o false, según corresponda; y que además respete las normas y buenas prácticas dadas en clase, y sea eficiente (evite ciclos innecesario).
# Además agregue 4 casos de prueba, para testear con doctest, uno con su número de legajo (padrón) de la facultad, otro con su DNI, otro con su edad y otro con el primer número primo posterior a su número de legajo.
# Fuera de la función, debe haber un print(doctest.testmod()) para ejecutar las pruebas.
# Entrega: Suba a la caja de texto el código generado, y entregue 2 archivos: uno el archivo .py, y el otro una imagen que muestre la ejecución en su computadora. El nombre de los archivos debe ser su número de legajo.

import doctest

def validar_numero(numero):
    """Funcion que valida que el numero no sea menor o igual a 1.
    
    >>> validar_numero(17) # Numero positivo mayor a 1
    True
    >>> validar_numero(0) # Numero nulo
    False
    >>> validar_numero(-5) # Numero negativo
    False
    """
    return numero > 1

def es_primo(numero):
    """Funcion que determina si un numero es primo o no iterando desde 2 hasta la raiz cuadrada del numero,
    y que devuelve True o False segun corresponda.
    
    >>> es_primo(114547)  # Numero de legajo
    True
    >>> es_primo(41639148)  # DNI
    False
    >>> es_primo(27)  # Edad
    False
    >>> es_primo(114553)  # Primer numero primo posterior al legajo
    True
    """
    divisor = 2
    dividendo = numero**0.5
    if numero == 2:
        return True
    else:
        while divisor <= int(dividendo):
            if numero % divisor == 0:
                return False
            divisor += 1
        return True


def main():
    numero = int(input("Ingrese un numero para verificar si es primo: "))
    if validar_numero(numero):
        print(es_primo(numero))
    else:
        print("Numero invalido. Debe ser un entero mayor a 1.")

main()

print(doctest.testmod())




















# def validar_numero(numero):
#    """funcion que valida que el numero no sea menor o igual a 1 y si es un entero"""
#    if numero <= 1:
#        return False
#    elif not isinstance(numero, int):
#        return False
#    return True
# def es_primo(numero):
#    """funcion que determina si un numero es primo o no con el numero que le solicitamos al usuario,
#    y que devuelve True o False segun corresponda.
#    
#    casos de prueba:
#    >>> es_primo(114547)  # Numero de legajo
#    True
#    >>> es_primo(41639148)  # Dni
#    False
#    >>> es_primo(27)  # Edad
#    False
#    >>> es_primo(114553)  # Primer numero primo posterior al legajo
#    True
#    """
#    for i in range(2, int(numero**0.5) + 1):
#        if numero % i == 0:
#            return False
#    return True
#    ##
#
# def main():
#   numero = int(input("Ingrese un número para verificar si es primo: "))
#   valido = validar_numero(numero)
#    if valido:
#        if es_primo(numero):
#            print("True")
#        else:
#            print("False")
#    return
#
# main()
#
# import doctest
# print(doctest.testmod())