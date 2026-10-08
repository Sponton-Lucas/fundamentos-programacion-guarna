# Escribir una función que reciba por parámetro un texto, y devuelva un diccionario, el
# cual tendrá como claves, cada una de las palabras que hay en el texto, y como valor,
# la cantidad de ocurrencias de dicha palabra en el texto.
# No distinguir entre mayúsculas y minúsculas.
# Considerar que las palabras del texto estarán separadas por blancos.

frase = "Estaba estaba cola cola estaba estaba en mi casa haciendo tarea de la nada el dia se nublo, por lo que estaba haciendo frio asi que lo que hice fue prender la estufa"

def ocurrenciaTexto(texto):
    ocurrencias = {}
    
    for palabra in texto.lower().split():
        if palabra not in ocurrencias:
            ocurrencias[palabra] = 1
        else:
            ocurrencias[palabra] += 1
    return ocurrencias


resultado = ocurrenciaTexto(frase)
print(resultado)