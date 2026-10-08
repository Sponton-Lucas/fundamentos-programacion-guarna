# Escribir una función potencia que reciba dos enteros: a y b. 
# Debe retornar ab sin utilizar funciones de potencia o el operador **, solo con sumas, productos y divisiones.

def potencia(a, b):
    if b < 0:
        return 1 / potencia(a, -b)
    elif b == 0:
        return 1
    else:
        resultado = 1
        for j in range(b):
            resultado *= a
        return resultado

print(potencia(2, -2))