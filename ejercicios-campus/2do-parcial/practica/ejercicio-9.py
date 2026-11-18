
def leer_maestro(archivo):
    linea = archivo.readline()
    if linea:
        codigo, producto, stock = linea.strip().split(",")
        codigo = int(codigo)
        stock = int(stock)
    else:
        codigo = None
        producto = None
        stock = None
    return codigo, producto, stock

def leer_detalle(archivo):
    linea = archivo.readline()
    if linea:
        codigo, cantidad = linea.strip().split(",")
        codigo = int(codigo)
        cantidad = int(cantidad)
    else:
        codigo = None
        cantidad = None
    return codigo, cantidad

def actualizar(maestro, detalle, salida):
    cod_m, producto, stock = leer_maestro(maestro)
    cod_d, cantidad = leer_detalle(detalle)
    
    while cod_m is not None:
        if cod_m == cod_d:
            total_vendido = 0
            while cod_d is not None and cod_d == cod_m:
                total_vendido += cantidad
                cod_d, cantidad = leer_detalle(detalle)
            stock -= total_vendido
        salida.write(str(cod_m)+","+producto+","+str(stock)+"\n")
        cod_m, producto, stock = leer_maestro(maestro)

def main():
    maestro = open("maestro.csv")
    detalle = open("detalle.csv")
    salida = open("maestro_actualizado.csv", "w")
    actualizar(maestro, detalle, salida)
    maestro.close()
    detalle.close()
    salida.close()

main()