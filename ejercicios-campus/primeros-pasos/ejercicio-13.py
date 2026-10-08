# 1)Escribir un programa que solicite el ingreso de dos números y luego informe cuál es el mayor de los número ingresados. Suponer que siempre los números ingresados serán distintos.

# 2)Ahora, tomá el ejercicio anterior y considerá que el usuario podría ingresar dos veces el mismo número.

# 3)Escribir un programa que solicite el ingreso de un mes e informe el nombre del mes. Por ejemplo, si el usuario ingresa "1", se deberá mostrar: "Mes ingresado: Enero" En caso que el mes ingresado por el usuario no sea válido, deberá mostrar "Mes Ingresado: Inválido".

# 4)Solicitar el ingreso de un mes y un año e informar la cantidad de días del mes, considerando los años bisiestos.Tenga en cuenta que un año bisiesto es aquel dividible por 4, salvo que sea divisible por 100, en cuyo caso también debe ser divisible por 400.

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if numero1 > numero2:
    print(f"El mayor número ingresado es: {numero1}")
elif numero2 > numero1:
    print(f"El mayor número ingresado es: {numero2}")
else:
    print("Los números ingresados son iguales.")
    
    
mes = int(input("Ingrese un número de mes (1-12): "))
if mes == 1:
    print("Mes ingresado: Enero")
elif mes == 2:
    print("Mes ingresado: Febrero")
elif mes == 3:      
    print("Mes ingresado: Marzo")
elif mes == 4:
    print("Mes ingresado: Abril")
elif mes == 5:
    print("Mes ingresado: Mayo")
elif mes == 6:
    print("Mes ingresado: Junio")
elif mes == 7:
    print("Mes ingresado: Julio")
elif mes == 8:
    print("Mes ingresado: Agosto")
elif mes == 9:
    print("Mes ingresado: Septiembre")
elif mes == 10:
    print("Mes ingresado: Octubre")
elif mes == 11:
    print("Mes ingresado: Noviembre")
elif mes == 12:
    print("Mes ingresado: Diciembre")
else:
    print("Mes ingresado: Inválido")
    
# 5) Escribir un programa que le solicite al usuario el ingreso de una temperatura y la unidad en la que se encuentra (F ó C). Luego el programa debe mostrar la temperatura ingresada, convertida en la otra unidad. La relación entre temperaturas (C) Celsius y (F) Fahrenheit, está dada por: C=5/9∗(F−32)

temperatura = float(input("Ingrese la temperatura: "))
unidad = input("Ingrese la unidad de temperatura (C o F): ")
if unidad.upper() == "C":
    temperatura_fahrenheit = (temperatura * 9/5) + 32
    print(f"La temperatura ingresada es: {temperatura}°C, convertida a Fahrenheit es: {temperatura_fahrenheit}°F")
elif unidad.upper() == "F":
    temperatura_celsius = (temperatura - 32) * 5/9
    print(f"La temperatura ingresada es: {temperatura}°F, convertida a Celsius es: {temperatura_celsius}°C")
else:
    print("Unidad de temperatura inválida. Por favor ingrese 'C' para Celsius o 'F' para Fahrenheit.")