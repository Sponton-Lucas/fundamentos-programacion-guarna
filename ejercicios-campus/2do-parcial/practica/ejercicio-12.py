# peliculas_accion.csv = 1980,Rambo; 1990,Duro de Matar; 2000,Gladiador
# peliculas_comedia.csv = 1985,Volver al Futuro; 1995,Toy Story; 2005,Cars
# Se pide generar peliculas_completas.csv ordenada por el anio de menor a mayor
#si dos peliculas salieron el mismo anio primero la de accion luego la de comedia

def leer_peliculas(archivo):
    linea = archivo.readline()
    if linea:
        anio, titulo = linea.strip().split(",")
        anio = int(anio)
    else:
        anio = titulo = None
    return anio, titulo

def procesar_archivos(accion, comedia, salida):
    anio_a, titulo_a = leer_peliculas(accion)
    anio_c, titulo_c = leer_peliculas(comedia)
    
    while anio_a is not None and anio_c is not None:
        if anio_a <= anio_c:
            salida.write(str(anio_a)+","+titulo_a+",Accion\n")
            anio_a, titulo_a = leer_peliculas(accion)
        else:
            salida.write(str(anio_c)+","+titulo_c+",Comedia\n")
            anio_c, titulo_c = leer_peliculas(comedia)
    while anio_a is not None:
        salida.write(str(anio_a)+","+titulo_a+",Accion\n")
        anio_a, titulo_a = leer_peliculas(accion)
    while anio_c is not None:
        salida.write(str(anio_c)+","+titulo_c+",Comedia\n")
        anio_c, titulo_c = leer_peliculas(comedia)




def main():
    accion = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-12-peliculas_accion.csv")
    comedia = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-12-peliculas_comedia.csv")
    salida = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-12-peliculas_completas.csv", "w")
    procesar_archivos(accion, comedia, salida)
    accion.close()
    comedia.close()
    salida.close()

main()