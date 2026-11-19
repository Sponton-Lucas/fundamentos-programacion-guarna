# libros.csv, formato: codigo, titulo, stock
# prestamos.csv, formato: codigo, cantidad_prestado
# Se pide generar un archivo libros_actualizados.csv ocn el stock actualizado.

def leer_libros(libros):
    linea = libros.readline()
    if linea:
        codigo, titulo, stock = linea.strip().split(",")
        codigo = int(codigo)
        stock = int(stock)
    else:
        codigo = titulo = stock = None
    return codigo, titulo, stock

def leer_prestamos(prestamos):
    linea = prestamos.readline()
    if linea:
        codigo, cant_prestada = linea.strip().split(",")
        codigo = int(codigo)
        cant_prestada = int(cant_prestada)
    else:
        codigo = cant_prestada = None
    return codigo, cant_prestada

def actualizar(libros, prestamos, salida):
    cod_l, titulo, stock = leer_libros(libros)
    cod_p, cant_prestada = leer_prestamos(prestamos)
    max_prestamos = 0
    titulo_max = []
    while cod_l is not None:
        if cod_l == cod_p:
            total_prestado = 0
            while cod_p is not None and cod_p == cod_l:
                total_prestado += cant_prestada
                cod_p, cant_prestada = leer_prestamos(prestamos)
            if total_prestado > max_prestamos:
                max_prestamos = total_prestado
                titulo_max = [titulo]
            elif total_prestado == max_prestamos:
                titulo_max.append(titulo)
            stock -= total_prestado
        salida.write(str(cod_l)+","+titulo+","+str(stock)+"\n")
        cod_l, titulo, stock = leer_libros(libros)
    print("Libro/s mas prestados del mes:")
    for titulo in titulo_max:
        print(f"Titulo: {titulo}")
    print(f"Cantidad de prestamos: {max_prestamos}")

def main():
    libros = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-10-libros.csv")
    prestamos = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-10-prestamos.csv")
    salida = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-10-libros_actualizados.csv", "w")
    
    actualizar(libros, prestamos, salida)
    libros.close()
    prestamos.close()
    salida.close()

main()