def leer_venta(archivo):
    linea = archivo.readline()
    if linea:
        partes = linea.strip().split(",")
        codigo = int(partes[0])
        cantidad = int(partes[1])
        facturado = float(partes[2])
    else:
        codigo = None
        cantidad = None
        facturado = None
    return codigo, cantidad, facturado

# Hecho el obtener minimo con for
# def obtener_minimo_codigo(c1, c2, c3, c4):
#    minimo = None
#    for c in (c1, c2, c3, c4):
#        if c is not None and (minimo is None or c < minimo):
#            minimo = c
#    return minimo
# Hecho solo con ifs
def obtener_minimo_codigo(c1, c2, c3, c4):
    minimo = None

    if c1 is not None and (minimo is None or c1 < minimo):
        minimo = c1

    if c2 is not None and (minimo is None or c2 < minimo):
        minimo = c2

    if c3 is not None and (minimo is None or c3 < minimo):
        minimo = c3

    if c4 is not None and (minimo is None or c4 < minimo):
        minimo = c4

    return minimo

def procesar_sucursal(archivo, codigo_actual, cantidad_actual, facturado_actual, codigo_objetivo):
    total_cant = 0
    total_fact = 0.0
    vendio = 0

    while codigo_actual is not None and codigo_actual == codigo_objetivo:
        total_cant += cantidad_actual
        total_fact += facturado_actual
        vendio = 1
        codigo_actual, cantidad_actual, facturado_actual = leer_venta(archivo)

    return total_cant, total_fact, vendio, codigo_actual, cantidad_actual, facturado_actual


def procesar_archivos(v1, v2, v3, v4, salida):
    c1, cant1, fact1 = leer_venta(v1)
    c2, cant2, fact2 = leer_venta(v2)
    c3, cant3, fact3 = leer_venta(v3)
    c4, cant4, fact4 = leer_venta(v4)

    while c1 is not None or c2 is not None or c3 is not None or c4 is not None:
        codigo_min = obtener_minimo_codigo(c1, c2, c3, c4)

        total_vendido = 0
        total_facturado = 0.0
        sucursales_vendieron = 0

        cant_s1, fact_s1, v_s1, c1, cant1, fact1 = procesar_sucursal(v1, c1, cant1, fact1, codigo_min)
        cant_s2, fact_s2, v_s2, c2, cant2, fact2 = procesar_sucursal(v2, c2, cant2, fact2, codigo_min)
        cant_s3, fact_s3, v_s3, c3, cant3, fact3 = procesar_sucursal(v3, c3, cant3, fact3, codigo_min)
        cant_s4, fact_s4, v_s4, c4, cant4, fact4 = procesar_sucursal(v4, c4, cant4, fact4, codigo_min)

        total_vendido = cant_s1 + cant_s2 + cant_s3 + cant_s4
        total_facturado = fact_s1 + fact_s2 + fact_s3 + fact_s4
        sucursales_vendieron = v_s1 + v_s2 + v_s3 + v_s4

        salida.write(f"{codigo_min},{total_vendido},{total_facturado:.2f},{sucursales_vendieron}\n")


def main():
    v1 = open("ventas01.csv", "r")
    v2 = open("ventas02.csv", "r")
    v3 = open("ventas03.csv", "r")
    v4 = open("ventas04.csv", "r")
    salida = open("ventas_diarias.csv", "w")

    procesar_archivos(v1, v2, v3, v4, salida)

    v1.close()
    v2.close()
    v3.close()
    v4.close()
    salida.close()


if __name__ == "__main__":
    main()