# ventas.csv formato= vendedor, mes, importe
# Informar para cada vendedor el importe de cada mes y el total
# ej: vendedor: juan
#   mes 1: 15000
#   mes 2: 10000
#   mes 5: 4000
#   total vendedor: 29000

def leer_ventas(ventas):
    linea = ventas.readline()
    if linea:
        vendedor, mes, importe = linea.strip().split(",")
        mes = int(mes)
        importe = int(importe)
    else:
        vendedor = mes = importe = None
    return vendedor, mes, importe

def procesar_ventas(ventas):
    vendedor, mes, importe = leer_ventas(ventas)
    while vendedor is not None:
        vendedor_actual = vendedor
        total_vendedor = 0
        print(f"Vendedor: {vendedor_actual}")
        while vendedor is not None and vendedor == vendedor_actual:
            mes_actual = mes
            total_mes = 0
            while vendedor is not None and vendedor == vendedor_actual and mes == mes_actual:
                total_mes += importe
                vendedor, mes, importe = leer_ventas(ventas)
            print(f"Mes {mes_actual}: {total_mes}")
            total_vendedor += total_mes
        print(f"Total vendedor: {total_vendedor}")

def main():
    ventas = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-13-ventas.csv")
    procesar_ventas(ventas)
    ventas.close()

main()