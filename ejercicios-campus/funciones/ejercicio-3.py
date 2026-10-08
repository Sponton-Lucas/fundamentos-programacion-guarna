#Escribir una función que reciba un valor y calcule el factorial del mismo.
#Si no se puede calcular el factorial del valor recibido, la función deberá devolver 0, de lo contrario deberá devolver el valor calculado.
#No debe imprimir el valor, debe solamente devolverlo.
#Probá la función invoncándola desde el bloque principal, con al menos 3 valores.

def calcularFactorial(numero):
    if numero <= 1:
        return 0
    else:
        factorial = 1
        for i in range(1, numero+1):
            factorial *= i
        return factorial


print(calcularFactorial(-4))
print(calcularFactorial(4))
print(calcularFactorial(5))
print(calcularFactorial(6))