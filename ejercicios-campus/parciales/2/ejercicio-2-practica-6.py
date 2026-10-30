# Implementar generar_descuentos_clientes, con parametros: compras, clientes_vip, descuento_base. Donde 
# compras = [[101,5000],[205,7000],[101,3000]] cada elemento representa: [id_cliente, monto_compra]
# La lista esta ordenada cronologicamente. La funcion debe devolver una nueva lista con: [id_cliente,descuento]
# solamente para los clientes que pertenezcan a clientes_vip.
# La primera compra de un cliente VIP recibe descuento_base. Si ese mismo cliente ya tenia una compra anterior registrada
# el descuento aumenta un 20%

def generar_descuentos_clientes(compras, clientes_vip, descuento_base):
    listas_clientes = []
    aparicion_vip = []
    
    for id_cliente, monton_compra in compras:
        if id_cliente in clientes_vip:
            if id_cliente in aparicion_vip:
                descuento = descuento_base * 1.2
            else:
                descuento = descuento_base
                aparicion_vip.append(id_cliente)
            listas_clientes.append([id_cliente, descuento])
    return listas_clientes