# 1) Escribir una funcion contar que reciba una cadena de caracteres y devuelve un entero que indica la cantidad de
#caracteres alfabeticos distintos que tiene la cadena.No debe distinguir mayusculas de minusculas ni caracteres con tilde.

def contar(cadena):
    cantidadCaracteres = 0
    caracteresDistintos = []
    acentos = "áéíóú"
    for letra in cadena.lower():
        if letra.isalpha() and letra not in caracteresDistintos and letra not in acentos:
            caracteresDistintos.append(letra)
            cantidadCaracteres += 1
    print(caracteresDistintos)
    return cantidadCaracteres
