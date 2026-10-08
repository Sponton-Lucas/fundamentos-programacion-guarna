# 2) Solicitar el ingreso de 2 valores enteros y luego informar el resultado de multiplicarlos, pero mediante sumas sucesivas. Optimizar el algoritmo, realizando la menor cantidad de ciclos posibles. Tener en cuenta que el usuario puede ingresar valores negativos. Para la solución NO PUEDE utilizar la función abs().

### OPCION 1 
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

sumasSucesivas = 0
if numero1 == 0 or numero2 == 0:
    sumasSucesivas = 0
elif numero1 > 0 and numero2 > 0:
    for i in range(numero2):
        sumasSucesivas += numero1
elif numero1 < 0 and numero2 < 0:
    for i in range(-numero2):
        sumasSucesivas += -numero1
elif numero1 > 0 and numero2 < 0:
    for i in range(-numero2):
        sumasSucesivas += -numero1
elif numero1 < 0 and numero2 > 0:
    for i in range(numero2):
        sumasSucesivas += numero1
print("El resultado de la multiplicación es:", sumasSucesivas)


### OPCION 2
#numero1 = int(input("Ingrese el primer número entero: "))
#numero2 = int(input("Ingrese el segundo número entero: "))

# Inicializamos acumulador
#sumasSucesivas = 0

# Caso especial: si alguno es 0
#if numero1 == 0 or numero2 == 0:
#    sumasSucesivas = 0
#else:
    # Determinar el signo del resultado
#    signo = 1
#    if (numero1 < 0 and numero2 > 0) or (numero1 > 0 and numero2 < 0):
#        signo = -1

    # Convertimos ambos a positivos "a mano"
#    if numero1 < 0:
#        numero1 = -numero1
#    if numero2 < 0:
#        numero2 = -numero2

    # Hacemos la suma sucesiva
#    for i in range(numero2):
#        sumasSucesivas += numero1

    # Aplicamos el signo al resultado final
#    sumasSucesivas *= signo

#print("El resultado de la multiplicación es:", sumasSucesivas)
