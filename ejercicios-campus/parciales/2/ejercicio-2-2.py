#2) Escribir una funcion elegir_comidas en python que reciba una lista de listas, cada sublista es una comida, en donde
# el primer elemento es el nombre de la comida y los siguientres elementos los respectivos ingredientes. Tambien recibe
# una lista de ingredientes prohibidos. Debe devolver una lista con los nombres de las comidas permitidas(no deben
# contener ingredientes prohibidos)
#Ejemplo:
comidas = [["milanesa", "bifes de nalga", "pan rallado", "huevo"],
["ravioles", "harina", "espinaca", "ricota"],
["pizza", "queso", "harina", "tomate", "aceitunas"]]
prohibidos_1 = ["huevo", "nueces", "aceitunas"]
prohibidos_2 = ["huevo", "nueces"]
#elegir_comidas(comidas, prohibidos_1) --->['ravioles']
#elegir_comidas(comidas, prohibidos_2) --->['ravioles', 'pizza']
#Testea la funcion con dos casos usando doctest, con 2 listas de prohibidos distintas a las del ejemplo.

def elegir_comidas(comidas, prohibidos):
    """
    >>> comidas1 = [
    ...     ["milanesa", "bife", "pan rallado", "huevo"],
    ...     ["ravioles", "harina", "ricota"],
    ...     ["pizza", "queso", "aceitunas"],
    ...     ["hamburguesa", "carne", "pan"]
    ... ]

    >>> comidas2 = [
    ...     ["ensalada", "lechuga", "tomate"],
    ...     ["tarta", "harina", "espinaca"],
    ...     ["empanadas", "carne", "cebolla"],
    ...     ["pastas", "harina", "huevo"]
    ... ]

    >>> elegir_comidas(comidas1, ["huevo", "aceitunas"])
    ['ravioles', 'hamburguesa']

    >>> elegir_comidas(comidas1, ["harina", "carne"])
    ['milanesa', 'pizza']

    >>> elegir_comidas(comidas2, ["tomate", "huevo"])
    ['tarta', 'empanadas']

    >>> elegir_comidas(comidas2, ["cebolla", "espinaca"])
    ['ensalada', 'pastas']
    """

    permitidas = []

    for comida in comidas:

        nombre = comida[0]
        ingredientes = comida[1:]

        valida = True

        for ingrediente in ingredientes:

            if ingrediente in prohibidos:
                valida = False

        if valida:
            permitidas.append(nombre)

    return permitidas


if __name__ == "__main__":
    import doctest
    doctest.testmod()