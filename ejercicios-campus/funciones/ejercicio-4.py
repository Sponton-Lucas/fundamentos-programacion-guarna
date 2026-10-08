#Escribir una función que reciba un valor y si el valor recibido no es mayor a 0, envíe un mensaje de error diciendo "ERROR: El valor a ingresar debe ser mayor a 0", y vuelva a solicitar el ingreso de un valor y evaluar si cumple con la condición. Debe repetirse hasta que el usuario haya ingresado un valor mayor a 0.
#La función debe devolver un valor válido.

numero = int(input("Ingrese un numero a analizar: "))

def mayorA(numero):
    while numero <= 0:
        print("ERROR: El valor a ingresar debe ser mayor a 0.")
        numero = int(input("Ingrese un numero a analizar: "))


mayorA(numero)