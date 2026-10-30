# Implementar la funcion calcular_monto_vendedores, que reciba por parametro: ventas, vendedores_habilitados, comision
# y devuelva el monto total de comisiones a pagar.
# La lista de ventas contiene elementos con el formato: [id_vendedor, monto_venta]
# por ej: [[101, 5000],[300,7000],[101,2000],[205,10000]]
# La lista vendedores_habilitados contiene los IDs de los vendedores cuyas ventas generan comision.
# Por ej: [101,205]. El valor comision representa el porcentaje de comision sobre cada venta
# Por ejL 10 representa un 10%.
# Restricciones: si el vendedor no esta en vendedores_habilitados, su venta debe ignorarse. Las primeras 3 ventas validas
# generan la comision completa. A partir de la cuarta venta valida inclusive, la comision de esa venta recibe un bono del 50%

def calcular_monto_vendedores(ventas, vendedores_habilitados, comision):
    total_comisiones = 0
    ventas_validas = 0
    
    for id_vendedor, monto_venta in ventas:
        if id_vendedor in vendedores_habilitados:
            ventas_validas += 1
            
            tarifa = monto_venta * comision / 100
            
            if ventas_validas >= 4:
                tarifa += tarifa / 2
            
            total_comisiones += tarifa
    return total_comisiones