# Escribir una función que reciba por parámetro un diccionario con el siguiente formato:
# { id_producto: [ stock_minimo, stock_actual ],..........}, donde el id_producto será la
# clave, de tipo cadena; y la lista asociada a cada clave id_producto, contendrá una
# dupla de valores, siendo el primero, el stock mínimo a mantener de dicho producto; y
# el segundo, el stock actual del producto; ambos de tipo entero positivo.
# La función debe imprimir un listado con los productos a reponer (cuyo stock_actual
# sea menor al stock_minimo), indicando el id_producto y la cantidad a reponer

diccionario = { "1": [ 8, 6], "2": [ 15, 6], "3": [ 10, 12]}



def reponerProducto(dic):
    productoRestock = {}
    
    for clave, (stockMinimo, stockActual) in dic.items():
        if stockActual < stockMinimo:
            productoRestock[clave] = stockMinimo - stockActual

    if len(productoRestock) == 0:
        print("No hay producto para reponer.")
    else:
        for clave, cantidad in productoRestock.items():
            print(f"Producto {clave}: reponer {cantidad} unidades")

reponerProducto(diccionario)
