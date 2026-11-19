# Se dispone de dos archivos ordenados por codigo de producto.
# productos.csv : 1001,Mouse,50; 1002,Teclado,30; 1003,Monitor,20; 1004,Webcam,10
# Formato es: codigo, nombre, stock
# ingresos.csv: 1001,5; 1001,3; 1003,2; 1004,10; 1004,5
# Formato: codigo, cantidad_ingresada
# Se pide generar un archivo productos_actualizados.csv donde el stock quede incrementado segun los ingresos.
# Ademas informar el producto con mayor cantidad de unidades ingresadas.
# En caso de empate mostrar todos los productos empatados.

def leer_producto(productos):
    linea = productos.readline()
    if linea:
        codigo_p, nombre, stock = linea.strip().split(",")
        codigo_p = int(codigo_p)
        stock = int(stock)
    else:
        codigo_p = nombre = stock = None
    return codigo_p, nombre, stock

def leer_ingreso(ingresos):
    linea = ingresos.readline()
    if linea != "":
        codigo_i, cant_ingresada = linea.strip().split(",")
        codigo_i = int(codigo_i)
        cant_ingresada = int(cant_ingresada)
    else:
        codigo_i = cant_ingresada = None
    return codigo_i, cant_ingresada

def procesar_archivos(productos, ingresos, productos_actualizados):
    codigo_p, nombre, stock = leer_producto(productos)
    codigo_i, cant_ingresada = leer_ingreso(ingresos)
    while codigo_p != None:
        total_ingresos = 0
        if codigo_p == codigo_i:
            
            while codigo_i != None and codigo_i == codigo_p:
                total_ingresos += cant_ingresada
                codigo_i, cant_ingresada = leer_ingreso(ingresos)
        stock += total_ingresos
        productos_actualizados.write(str(codigo_p)+","+nombre+","+str(stock)+"\n")
        codigo_p, nombre, stock = leer_producto(productos)


def main():
    productos = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-15-productos.csv")
    ingresos = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-15-ingresos.csv")
    productos_actualizados = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-15-productos_actualizados.csv", "w")
    procesar_archivos(productos, ingresos, productos_actualizados)
    productos.close()
    ingresos.close()
    productos_actualizados.close()

main()