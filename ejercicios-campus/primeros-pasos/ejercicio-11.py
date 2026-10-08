# 1) Escribir un programa que solicite el ingreso del radio de un circulo y luego calcule e informe su diametro, su perimetro y su superficie-
# 2) Solicitar el ingreso de tres palabras y luego mostrar todas las frases posibles, resultantes de combinar las 3 palabras ingresadas.

radio = float(input("Ingrese el radio del circulo: "))
diametro = radio * 2
perimetro = 2 * 3.14 * radio
superficie = 3.14 * radio ** 2

print(f"El diametro del circulo es: {diametro}")
print(f"El perimetro del circulo es: {perimetro}")
print(f"La superficie del circulo es: {superficie}")

palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
palabra3 = input("Ingrese la tercera palabra: ")

print(f"{palabra1} {palabra2} {palabra3}")
print(f"{palabra1} {palabra3} {palabra2}")
print(f"{palabra2} {palabra1} {palabra3}")
print(f"{palabra2} {palabra3} {palabra1}")
print(f"{palabra3} {palabra1} {palabra2}")
print(f"{palabra3} {palabra2} {palabra1}")