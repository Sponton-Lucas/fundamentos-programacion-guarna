# Implementar ranking_productos(ventas, productos)
# ventas contiene [id_producto, cantidad], por ej: [[10,3],[20,1],[10,2],[30,5],[20,4]]
# y productos contiene [id_producto, nombre], por ej: [[10,"Mouse"],[20,"Teclado"],[30,"Monitor"]]
# Calcular cuantas unidades vendidas tiene cada producto. La funcion debe devolver una lista con el formato: 
# [[nombre_producto, total_vendido]] ordenada de mayor a menor cantidad vendida.
# No usar diccionarios , sort() o sorted()

def ranking_productos(ventas, productos):

    resultado = []

    # Construcción de la lista [nombre, total_vendido]

    for id_producto_p, nombre in productos:

        total_vendido = 0

        for id_producto_v, cantidad in ventas:

            if id_producto_v == id_producto_p:
                total_vendido += cantidad

        resultado.append([nombre, total_vendido])

    # Ordenamiento de mayor a menor

    for i in range(len(resultado)):

        for j in range(i + 1, len(resultado)):

            if resultado[j][1] > resultado[i][1]:

                aux = resultado[i]
                resultado[i] = resultado[j]
                resultado[j] = aux

    return resultado