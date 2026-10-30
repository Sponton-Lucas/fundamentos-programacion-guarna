# Implementar calcular_facturacion_clientes, con parametros: compras, productos, clientes_vip
# La lista compras tiene [id_cliente, id_producto, cantidad]. Por ej: [[101,10,2],[205,20,1][101,20,3],[101,10,1]]
# La lista productos contiene: [id_producto, nombre, precio], Por ej: [[10,"Mouse",1000],[20,"Teclado",3000]]
# La lista clientes_vip contiene [101, 300].
# Debe devolver una lista de la forma: [id_cliente, importe].
#Reglas: Solo se consideran compras de cliente vip. El importe de una compra es cantidad * precio.
# Si un cliente vip ya realizo una compra anterior valida, obtiene un descuento del 10% sobre esa compra.
# Cada compra valida debe generar una fila en la salida.
# Debe mantenerse el orden cronologico de las compras.

def calcular_facturacion_clientes(compras, productos, clientes_vip):

    importe_cliente = []
    cliente_compra_valida = []

    for id_cliente, id_producto_c, cantidad in compras:

        if id_cliente in clientes_vip:

            for id_producto_p, nombre, precio in productos:

                if id_producto_c == id_producto_p:

                    importe = cantidad * precio

                    if id_cliente in cliente_compra_valida:
                        importe = importe * 0.9
                    else:
                        cliente_compra_valida.append(id_cliente)

                    importe_cliente.append([id_cliente, importe])

    return importe_cliente