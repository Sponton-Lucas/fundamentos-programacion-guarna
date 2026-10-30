# 3) Escribir un programa modular( compuesto por funciones) en phyton que resuelva la siguiente problematica de gestion de
# infracciones de velocidad del centro de monitoreo de multas:
# PROCESAMIENTO DE DATOS: Obtener la lista con los datos de infracciones a procesar mediante la funcion obtener_infracciones() 
# que pertenece a la libreria peajes. Cada elemento de esta lista es una sublista que representa una infraccion detectada y
# contiene tres valores; (1)La patente(string),(2)La velocidad registrada(entero), y (3)El valor de la multa(flotante).
# Una misma patente puede repetirse si cometio mas de una infraccion. Procesar la lista y generar un diccionario llamado
# multas_por_patente. Este diccionario debera tener como clave la patente del vehiculo, y como valores, la velocidad maxima alcanzada
# por esa patente, lacantidad total de multas recibidas, y el total acumulado en dinero de las multas.
# ANALISIS DE RENDIMIENTO: Informar la o las patentes que alcanzaron la mayor velocidad registrada en el sistema. Nose pueden
# ordenar los datos para este paso y la estructura de datos solo puede ser recorrida una unica vez para obtener los resultados.
# INFORME DE VENTAS: Mostrar por pantalla de mayor a menor las patentes segun el total acumulado de multas. Los datos
# deben presentarse prolijamente en tres columnas: una para la patente, otra para la cantidad total de multas, y la ultima
# para el total de dinero acumulado en multas.

from peajes import obtener_infracciones


def generar_multas(infracciones):
    multas_por_patente = {}
    
    for patente, vel_registrada, valor_multa in infracciones:
        if patente in multas_por_patente:
            multas_por_patente[patente][1] += 1
            multas_por_patente[patente][2] += valor_multa
            if vel_registrada > multas_por_patente[patente][0]:
                multas_por_patente[patente][0] = vel_registrada
        else:
            multas_por_patente[patente] = [vel_registrada, 1, valor_multa]
    return multas_por_patente

def analisis_rendimiento(multas_por_patente):
    maximo = None
    mayor_velocidad = []
    for patente in multas_por_patente:
        vel_max = multas_por_patente[patente][0]
        if maximo == None or vel_max > maximo:
            maximo = vel_max
            mayor_velocidad = [patente]
        elif vel_max == maximo:
            mayor_velocidad.append(patente)
    print("Patentes con mayor velocidad registrada:")
    for patente in mayor_velocidad:
        print(patente, "-", maximo)

def informe_multas(multas_por_patente):
    ordenado = sorted(multas_por_patente.items(), key=lambda x: x[1][2], reverse=True)
    print("PATENTE\t\t CANTIDAD DE MULTAS\t\t TOTAL DE DINERO DE MULTAS")
    for patente, (vel_max, cant_multas, total_multas) in ordenado:
        print(f"{patente}\t\t{cant_multas}\t\t{total_multas}")

def main():
    infracciones = obtener_infracciones()
    multas_por_patente = generar_multas(infracciones)
    analisis_rendimiento(multas_por_patente)
    informe_multas(multas_por_patente)