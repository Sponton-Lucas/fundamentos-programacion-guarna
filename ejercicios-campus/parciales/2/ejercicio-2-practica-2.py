# implementar contar_productos_categoria, parametros: productos, categoria_buscada.
#donde productos=[["leche","lacteos",30],["yogur","lacteos",20],["pan","panaderia",50]]cada elementos
#representa [nombre, categoria, stock]
# La funcion debe devolver la cantidad total de unidades en stock de todos los productos que pertenecen a categoria_buscada.
# Por ej: contar_productos_categoria(productos,"lacteos") debe devolver 50 (leche 30 + yogur 20 = 50)

def contar_productos_categoria(productos, categoria_buscada):
    unidades_stock = 0
    
    for nombre,categoria,stock in productos:
        if categoria == categoria_buscada:
            unidades_stock += stock
    return unidades_stock