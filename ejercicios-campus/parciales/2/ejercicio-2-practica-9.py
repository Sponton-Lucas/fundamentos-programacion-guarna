#Implementar generar_comisiones, que reciba por parametro: ventas, productos, comision_base.La lista ventas contiene:
# [id_producto, cantidad]. Por ej: [[10,5],[20,2],[10,3],[30,7]]. La lista esta ordenada cronologicamente.La lista 
# productos contiene: [id_producto, nombre_producto, precio]. Por ej: [[10,"Mouse",1000],[20,"Teclado",3000],[30,"Monitor",5000]]
# La funcion debe devolver una nueva lista = [nombre_producto, comision]
# Reglas: Cada venta genera una comision. La comision normal es cantidad * comision_base.
# Si ese producto ya tuvo una venta anterior registrada en la lista ventas, la comision de esa venta debe incrementarse
# un 25%. Deben aparecer en el mismo orden cronologico de las ventas.
# Si ventas esta vacia, devolver []


def generar_comisiones(ventas, productos, comision_base):
    lista_comisiones = []
    ya_registrada = []
    
    for id_producto_v, cantidad in ventas:
        for id_producto_p, nombre_producto, precio in productos:
            if id_producto_v == id_producto_p:
                if id_producto_v in ya_registrada:
                    comision = cantidad * (comision_base * 1.25)
                else:
                    comision = cantidad * comision_base
                    ya_registrada.append(id_producto_v)
                lista_comisiones.append([nombre_producto, comision])
    return lista_comisiones