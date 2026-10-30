# Escribir un programa modular( compuesto por funciones) que resuelva la siguiente problematica.
# PROCESAMIENTO DE DATOS: Obtener la lista de ventas mediante la funcion obtener_ventas() que pertenece a la biblioteca
# libreria. Cada elemento de la lista representa una venta realizada y contiene: (1) Codigo del libro(string), (2) Cantidad
# de ejemplares vendidos(entero), (3) Importe de venta(float). Ej: [["A123",4,12000],["B456",2,8000],["A123",1,3000]]
# Un mismo codigo puede aparecer varias veces. Procesar la lista y generar un diccionario llamado: venta_por_libro, 
# donde la clave sea el codigo del libro, el valor sea una lista con: la mayor cantidad de ejemplares vendidos en una unica
# venta, la cantidad total de ventas realizadas, el importe total acumulado.
# ANALISIS DE RENDIMIENTO: Informar el o los codigos de libro que registraron la mayor cantidad de ejemplares vendidos
# en una unica venta. No se pueden ordenar los datos para este paso. La estructura de datos solo puede ser recorrida una unica vez
# para obtener el resultado.
# INFORME DE VENTAS: Mostrar por pantalla, de mayor a menor segun el importe total acumulado: codigo del libro, cantidad
# total de ventas, importe total acumulado.

from libreria import obtener_ventas

def generar_diccionario(ventas):
    venta_por_libro = {}
    for cod_libro, cantidad_vendida, importe_venta in ventas:
        if cod_libro in venta_por_libro:
            if cantidad_vendida > venta_por_libro[cod_libro][0]:
                venta_por_libro[cod_libro][0] = cantidad_vendida
            venta_por_libro[cod_libro][1] += 1
            venta_por_libro[cod_libro][2] += importe_venta
        else:
            venta_por_libro[cod_libro] = [cantidad_vendida, 1, importe_venta]
    return venta_por_libro

def analisis_rendimiento(venta_por_libro):
    mayor = None
    may_vendidos = []
    
    for libro in venta_por_libro:
        mayores_ventas = venta_por_libro[libro][0]
        if mayor == None or mayores_ventas > mayor:
            mayor = mayores_ventas
            may_vendidos = [libro]
        elif mayores_ventas == mayor:
            may_vendidos.append(libro)
    print("Libros que registraron mayor cantidad de ejemplares vendidos en una unica venta:")
    for libro in may_vendidos:
        print(libro, "-", mayor)

def informe_ventas(venta_por_libro):
    ordenado = sorted(venta_por_libro.items(), key=lambda x: x[1][2], reverse=True)
    print(f"CODIGO DEL LIBRO\t\tCANTIDAD TOTAL DE VENTAS\t\tIMPORTE TOTAL ACUMULADO")
    for cod_libro, (cant_unica_venta, cant_venta, total_acumulado) in ordenado:
        print(f"{cod_libro}\t\t{cant_venta}\t\t{total_acumulado}")



def main():
    ventas = obtener_ventas()
    venta_por_libro = generar_diccionario(ventas)
    analisis_rendimiento(venta_por_libro)
    informe_ventas(venta_por_libro)