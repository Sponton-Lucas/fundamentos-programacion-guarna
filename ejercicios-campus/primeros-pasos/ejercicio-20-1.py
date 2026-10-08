# 1) Escribir un programa que solicite el ingreso de números, y a medida que se ingresan, calcule e informe el factorial de cada número. Para saber si el programa debe seguir solicitando ingresos, se le debe preguntar al usuario si desea ingresar otro número.En caso que no se pueda calcular el factorial del número ingresado, se debe informar que no es posible calcular el factorial para dicho número.


verdadero = True
while verdadero:
    numero = int(input("Ingrese un número para calcular su factorial: "))
    
    if numero < 0:
        print("No es posible calcular el factorial de un número negativo.")
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        print(f"El factorial de {numero} es: {factorial}")
    
    continuar = input("¿Desea ingresar otro número? (s/n): ")
    if continuar.lower() != 's':
        verdadero = False