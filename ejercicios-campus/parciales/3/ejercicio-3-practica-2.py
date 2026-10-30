# Escribir un programa modular (compuesto por funciones) que resuelva la siguiente problematica:
# PROCESAMIENTO DE DATOS: Obtener una lista de prestamos mediante la funcion obtener_prestamos() perteneciente a la biblioteca biblioteca.
# Cada elemento de la lista representa un prestamo realizado y contiene: (1) Codigo del socio(string), (2) Cantidad de libros prestados en esa operacion(entero)
# (3) Dias de duracion del prestamo (entero). Por ej: [["SOC001",3,15],["SOC002",2,10],["SOC001",1,7]]. Un mismo socio puede aparecer varias veces.
# Procesar la lista y generar un diccionario llamado: prestamos_por_socio donde: la clave sea el codigo del socio,y el valor sea una lista con:
# la mayor cantidad de libros prestados en una unica operacion, la cantidad total de prestamos realizados, el total acumulado de libros prestados.
# ANALISIS DE ACTIVIDAD: Informar el o los socios que realizaron la operacion con mayor cantidad de libros prestados. Para este paso: no se pueden ordenar los
# datos, la estructura de datos solo puede ser recorrida una unica vez para obtener el resultado.
# INFORME GENERAL: Mostrar por pantalla los socios ordenados de mayor a menor segun el total acumulado de libros prestados.
# Mostrar: codigo de socio, cantidad total de prestamos realizados, total de libros prestados.

from biblioteca import obtener_prestamos

def generar_diccionario(prestamos):
    prestamos_por_socio = {}
    for cod_socio, cant_libros_operacion, dias_duracion_prestamo in prestamos:
        if cod_socio in prestamos_por_socio:
            if cant_libros_operacion > prestamos_por_socio[cod_socio][0]:
                prestamos_por_socio[cod_socio][0] = cant_libros_operacion
            prestamos_por_socio[cod_socio][1] += 1
            prestamos_por_socio[cod_socio][2] += cant_libros_operacion
        else:
            prestamos_por_socio[cod_socio] = [cant_libros_operacion, 1, cant_libros_operacion]
    return prestamos_por_socio

def analisis_actividad(prestamos_por_socio):
    mayor = None
    mayor_socios = []
    for cod_socio in prestamos_por_socio:
        mayor_cant_operacion = prestamos_por_socio[cod_socio][0]
        if mayor == None or mayor_cant_operacion > mayor:
            mayor = mayor_cant_operacion
            mayor_socios = [cod_socio]
        elif mayor_cant_operacion == mayor:
            mayor_socios.append(cod_socio)
    print("Socio/s que realizaron la operacion con mayor cantidad de libros prestados")
    for socio in mayor_socios:
        print(f"{socio} - {mayor}")

def informe_general(prestamos_por_socio):
    ordenado = sorted(prestamos_por_socio.items(), key=lambda x: x[1][2], reverse=True)
    print("CODIGO DE SOCIO\t\tCANTIDAD TOTAL DE PRESTAMOS REALIZADOS\t\tTOTAL DE LIBROS PRESTADOS")
    for socio, (mayor_cant_operacion, total_prestamos, total_prestados) in ordenado:
        print(f"{socio}\t\t{total_prestamos}\t\t{total_prestados}")

def main():
    prestamos = obtener_prestamos()
    prestamos_por_socio = generar_diccionario(prestamos)
    analisis_actividad(prestamos_por_socio)
    informe_general(prestamos_por_socio)