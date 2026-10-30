# Escribir un programa modular (compuesto por funciones) para resolver la siguiente problematica de una empresa de encomiendas.
#PROCESAMIENTO DE DATOS: Obtener la lista de envios mediante la funcion obtener_envios() perteneciente a la libreria correo.
# Cada elemento de la lista representa un envio realizado y contiene:
# 1) Codigo de cliente(entero).
# 2) Peso del paquete en kilogramos(float).
# 3) Importe pagado por el envio(float)
# Un mismo cliente puede aparecer mas de una vez si realizo varios envios.
# Generar un diccionario llamado estadisticas_clientes, cuya clave sea el codigo del cliente.
# Cada valor debera almacenar: mayor peso enviado por ese cliente, cantidad total de envios realizados, total gastado en envios.
# ANALISIS DE ACTIVIDAD: Informar el o los clientes que hayan realizado el envio de mayor peso registrado.
# No se permite ordenar los datos y la estructura solo puede recorrerse una vez para obtener el resultado.
# INFORME FINAL: Mostrar por pantalla los clientes ordenados de mayor a menor segun el dinero total gastado.
# Mostrar 3 columnas: Codigo de cliente - Cantidad de envios - Total gastado.


from correo import obtener_envios

def generar_diccionario(envios):
    estadisticas_clientes = {}
    
    for cod_cliente, peso_paquete, importe_envio in envios:
        if cod_cliente in estadisticas_clientes:
            estadisticas_clientes[cod_cliente][1] += 1
            estadisticas_clientes[cod_cliente][2] += importe_envio
            if peso_paquete > estadisticas_clientes[cod_cliente][0]:
                estadisticas_clientes[cod_cliente][0] = peso_paquete
        else:
            estadisticas_clientes[cod_cliente] = [peso_paquete, 1, importe_envio]
    return estadisticas_clientes

def analisis_actividad(estadisticas_clientes):
    mayor = None
    cliente_aparecio = []
    
    for cliente in estadisticas_clientes:
        peso_paquete = estadisticas_clientes[cliente][0]
        
        if mayor == None or peso_paquete > mayor:
            mayor = peso_paquete
            cliente_aparecio = [cliente]
        elif peso_paquete == mayor:
            cliente_aparecio.append(cliente)
    print("Clienters que realizaron el envio de mayor peso registrado")
    for cliente in cliente_aparecio:
        print(f"{cliente} - {mayor}")

def informe_final(estadisticas_clientes):
    ordenado = sorted(estadisticas_clientes.items(),key=lambda x: x[1][2], reverse=True)
    print("CODIGO CLIENTE\t\tCANTIDAD DE ENVIOS\t\tTOTAL GASTADO")
    for cod_cliente, peso_paquete, cant_envios, importe_envio in ordenado:
        print(f"{cod_cliente} - {cant_envios} - {importe_envio}")

def main():
    envios = obtener_envios()
    estadisticas_clientes = generar_diccionario(envios)
    analisis_actividad(estadisticas_clientes)
    informe_final(estadisticas_clientes)