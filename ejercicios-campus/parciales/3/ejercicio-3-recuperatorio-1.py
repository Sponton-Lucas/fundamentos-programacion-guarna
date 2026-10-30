from peajes import obtener_peaje

def generar_vehiculos(peajes):
    vehiculos = {}
    for patente, tipo, abono in peajes:
        if tipo in vehiculos:
            vehiculos[tipo][0] += 1
            vehiculos[tipo][1] += abono
        else:
            vehiculos[tipo] = [1, abono]
    return vehiculos

def analisis_rendimiento(vehiculos):
    minimo = None
    tipos_minimos = []
    for tipo in vehiculos:
        cantidad_pasadas = vehiculos[tipo][0]
        if minimo is None or cantidad_pasadas < minimo:
            minimo = cantidad_pasadas
            tipos_minimos = [tipo]
        elif cantidad_pasadas == minimo:
            tipos_minimos.append(tipo)
    print("Tipos con menor cantidad de pasadas:")
    for tipo in tipos_minimos:
        print(tipo, "-", minimo, "pasadas")

def informe_ventas(vehiculos):
    datos = []
    for tipo in vehiculos:
        cantidad_pasadas = vehiculos[tipo][0]
        total_recaudado = vehiculos[tipo][1]
        datos.append([tipo, cantidad_pasadas, total_recaudado])
    datos.sort(key=lambda x: x[2])
    print()
    print("TIPO\t\tPASADAS\t\tRECAUDADO")
    for tipo, pasadas, recaudado in datos:
        print(f"{tipo}\t\t{pasadas}\t\t{recaudado}")

def principal():
    peajes = obtener_peaje()
    vehiculos = generar_vehiculos(peajes)
    analisis_rendimiento(vehiculos)
    informe_ventas(vehiculos)

principal()