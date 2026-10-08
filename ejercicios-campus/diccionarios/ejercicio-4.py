#Escribir un programa que solicite el ingreso de un texto y luego informe un ranking de
#las palabras que aparecen en el texto.
#El texto ingresado debe tener como mínimo 20 palabras. En caso de no tener las
#palabras suficientes, solicitar se ingrese más texto, que debe ser agregado al ya
#existente.
#Considere palabras que sólo estén formadas por letras.
#Tenga en cuenta que seguido a una palabra, pueden estar los siguientes signos de
#puntuación: “,;.:”, en este caso, se debe quitar el signo.
#No debe diferenciar entre mayúsculas y minúsculas, por ejemplo: si aparecen en el
#texto las siguientes palabras: “sol”, “Sol”, “SOL”; se deben contabilizar 3 ocurrencias
#de la palabra “sol” como clave.
#No utilice métodos tales como count, find, index.
#Imprima el ranking, ordenado descendentemente, por la cantidad de ocurrencias de la
#palabra.

def validarTexto(texto):
    simbolos = ",;.:"
    for simbolo in simbolos:
        texto = texto.replace(simbolo, "")
    return [palabra.lower() for palabra in texto.split() if palabra.isalpha()]

def ingresoTexto():
    palabras = []
    
    while len(palabras) < 20:
        faltan = 20 - len(palabras)
        if faltan == 20:
            texto = input("Ingrese un texto de al menos 20 palabras: ")
        else:
            texto = input(f"Faltan {faltan} palabras. Ingrese mas texto: ")
        
        palabras.extend(validarTexto(texto))
    return palabras

def rankingPalabras(palabras):
    ranking = {}
    
    for palabra in palabras:
        if palabra not in ranking:
            ranking[palabra] = 1
        else:
            ranking[palabra] += 1
    return sorted(ranking.items(), key=lambda par: par[1], reverse=True)

def main():
    palabras = ingresoTexto()
    print(rankingPalabras(palabras))


main()