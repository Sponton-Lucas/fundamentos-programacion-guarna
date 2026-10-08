# Definir una funcion en python que reciba dos enteros y devuelva la division entera, pero sin utilizar las // (barras) */
#Siempre escribir una funcion main principal


def divisionEntera(dividendo, divisor):
	if divisor == 0:
		raise ValueError("No se puede dividir entre cero")

	dividendo_abs = abs(dividendo)
	divisor_abs = abs(divisor)
	cociente = 0
	resto = dividendo_abs

	while resto >= divisor_abs:
		resto -= divisor_abs
		cociente += 1

	if (dividendo < 0) != (divisor < 0):
		return -cociente if resto == 0 else -(cociente + 1)

	return cociente

def divisionEntera1():
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))
    try:
        resultado = divisionEntera(dividendo, divisor)
        print(f"El resultado de la división entera es: {resultado}")
    except ValueError as e:
        print(e)
    return resultado

divisionEntera1()