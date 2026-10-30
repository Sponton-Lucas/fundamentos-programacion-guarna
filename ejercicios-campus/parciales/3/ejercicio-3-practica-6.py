# Escribir un programa modular (compuesto por funciones) para resolver la siguiente problematica de una cadena de supermercados.
# PROCESAMIENTO DE DATOS: Obtener una lista mediante la funcion obtener_ventas() perteneciente a la libreria supermercado.
# Cada elemento de la lista representa una venta realizada durante el dia y contiene: (1) Codigo de producto(entero), (2) Cantidad vendida(entero)
# (3) Importe de la venta(float). Un producto puede aparecer varias veces porque pudo haberse vendido en distintas compras.
# Procesar la lista y generar un diccionario llamado ventas_productos. La clave sera el codigo del producto. Como valor debera almacenar:
# Mayor cantidad vendida en una unica venta, cantidad total de ventas realizadas, recaudacion total del producto.
# ANALISIS DE RENDIMIENTO: Informar el o los productos que registraron la mayor cantidad vendida en una unica venta. No se permite ordenar los datos.
# El diccionario solo puede recorrerse una vez para obtener el resultado.
# INFORME FINAL: Mostrar por pantalla los productos ordenados de mayor a menor segun su recaudacion total.
# Mostrar tres columnas: Codigo de producto, cantidad de ventas realizadas, recaudacion total.

from supermercado import obtener_ventas

def generar_diccionario(ventas):
    ventas_productos = {}
    
    for cod_producto, cantidad_vendida, importe_venta in ventas:
        if cod_producto in ventas_productos:
            ventas_productos[cod_producto][1] += 1
            ventas_productos[cod_producto][2] += importe_venta
            if cantidad_vendida > ventas_productos[cod_producto][0]:
                ventas_productos[cod_producto][0] = cantidad_vendida
        else:
            ventas_productos[cod_producto] = [cantidad_vendida, 1, importe_venta]
    return ventas_productos

def analisis_rendimiento(ventas_productos):
    mayor = None
    mayores_ventas = []
    
    for producto in ventas_productos:
        cantidad_vendida_unica_venta = ventas_productos[producto][0]
        if mayor == None or cantidad_vendida_unica_venta > mayor:
            mayor = cantidad_vendida_unica_venta
            mayores_ventas = [producto]
        elif cantidad_vendida_unica_venta == mayor:
            mayores_ventas.append(producto)
    print("Productos que registraron la mayor cantidad vendida en una unica venta:")
    for p in mayores_ventas:
        print(f"{p} - {mayor}")

def informe_final(ventas_productos):
    ordenado = sorted(ventas_productos.items(),key=lambda x: x[1][2], reverse=True)
    print("CODIGO DE PRODUCTO\t\tCANTIDAD DE VENTAS REALIZADAS\t\tRECAUDACION TOTAL")
    for cod_producto, (unica_vendida, cant_vendida, importe_total) in ordenado:
        print(f"{cod_producto}\t\t{cant_vendida}\t\t{importe_total}")

def main():
    ventas = obtener_ventas()
    ventas_productos = generar_diccionario(ventas)
    analisis_rendimiento(ventas_productos)
    informe_final(ventas_productos)