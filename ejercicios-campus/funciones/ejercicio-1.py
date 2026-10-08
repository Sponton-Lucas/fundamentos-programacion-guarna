#Escribir una función como la descripta en el video, pero que evalúe si el número recibido es impar, y en ese caso debe devolver True, de lo contrario debe devolver False.
#Probá la función invoncándola desde el bloque principal, con dos casos:
#Con tu número de tu legajo/padrón
#Con tu número de DNI

# funcion del video
# def es_par(numero):
#    if numero % 2 == 0:
#        devolver = True
#    else:
#        devolver = False
#    return devolver

#print("Es par" if (es_par(7)) else "Es Impar")

# def es_par2(numero):
#    """Devuelte True si el numero es par"""
#    return numero % 2 == 0
#print(es_par2(8))


def es_impar(numero):
    if numero % 2 != 0:
        devolver = True
    else:
        devolver = False
    return devolver

print(es_impar(114547))
print(es_impar(41639148))