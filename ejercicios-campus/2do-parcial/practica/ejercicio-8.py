# Generar un tercer archivo: Catalogo_Completo.csv ordenado por codigo de producto.
# 1001,Mouse ; 1002,Parlantes ; 1003,Teclado ....

def leer(archivo):
    linea = archivo.readline()
    if linea:
        codigo, nombre = linea.strip().split(",")
        codigo = int(codigo)
    else:
        codigo = None
        nombre = None
    return codigo, nombre

def procesar_archivo(archivo1, archivo2, salida):
    codigo1, nombre1 = leer(archivo1)
    codigo2, nombre2 = leer(archivo2)
    while codigo1 is not None and codigo2 is not None:
        if codigo1 < codigo2:
            salida.write(str(codigo1)+","+nombre1 + "\n")
            codigo1, nombre1 = leer(archivo1)
        else:
            salida.write(str(codigo2)+","+nombre2+"\n")
            codigo2, nombre2 = leer(archivo2)
    while codigo1 is not None:
        salida.write(str(codigo1)+","+nombre1+"\n")
        codigo1, nombre1 = leer(archivo1)
    while codigo2 is not None:
        salida.write(str(codigo2)+","+nombre2+"\n")
        codigo2, nombre2 = leer(archivo2)



def main():
    archivo1 = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/Productos_A.csv")
    archivo2 = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/Productos_B.csv")
    salida = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/Productos_C.csv", "w")
    
    procesar_archivo(archivo1, archivo2, salida)
    archivo1.close()
    archivo2.close()
    salida.close()

main()