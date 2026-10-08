# Escribir una funcion elegir_comidas en python que reciba una lista de listas, cada sublista es una comida en donde el primer
# elemento es el nombre de la comida y los siguientes elementos los respectivos ingredientes. Tambien recibe una lista de 
# ingredientes prohibidos. Debe devolver una lista con los nombres de las comidas permitidas.(no deben contener ingredientes prohibidos)
# ejemplo
# comidas = [["milanesa","bifes de nalga","pan rallado","huevo"],
#           ["ravioles","harina","espinaca","ricota"],
#           ["pizza","queso","harina","tomate","aceitunas"]]
#prohibidos_1 = ["huevos","nueces","aceitunas"]
#prohibidos_2 = ["huevo","nueces"]
#elegir_comidas(comidas, prohibidos_1) ---> ['ravioles']
#elegir_comidas(comidas, prohibidos_2) ---> ['ravioles','pizza']
# Testea la funcion usando doctest, para 2 listas de comidas de al menos 4 comidas cada una, y 3 listas de ingredientes
# prohibidos, con al menos 2 ingredientes cada una. Genera 4 casos de prueba diferentes.
import doctest
comidas_1 = [["milanesa","bifes de nalga","pan rallado","huevo"],
        ["ravioles","harina","espinaca","ricota"],
        ["pizza","queso","harina","tomate","aceitunas"],
        ["asado","vacio","chorizo","matambre"],
        ["ensalada","lechuga","tomate","cebolla","zanahoria"]]
comidas_2 = [["sopa","caldo","apio","zanahoria"],
            ["hamburguesa","carne picada","oregano","morron","pimienta"],
            ["tarta","jamon","queso"],
            ["empanada","pollo","huevo","aceitunas"]]
prohibidos_1 = ["huevo","nueces","aceitunas"]
prohibidos_2 = ["huevo","nueces"]
prohibidos_3 = ["chorizo","zanahoria"]
prohibidos_4 = ["cebolla","queso"]


def elegir_comidas(menu, prohibidos):
    """Funcion que pasados parametros una lista de comidas y una lista de ingredientes prohibidos devuelve una lista de las comidas
    que no contienen estos ingredientes.
    >>> elegir_comidas(comidas_1, prohibidos_1)
    ['ravioles', 'asado', 'ensalada']
    >>> elegir_comidas(comidas_1, prohibidos_2)
    ['ravioles', 'pizza', 'asado', 'ensalada']
    >>> elegir_comidas(comidas_2, prohibidos_3)
    ['hamburguesa', 'tarta', 'empanada']
    >>> elegir_comidas(comidas_2, prohibidos_4)
    ['sopa', 'hamburguesa', 'empanada']
    """
    comidas_permitidas = []
    for comida in menu:
        nombre = comida[0]
        ingredientes = comida[1:]
        prohibido_encontrado = False
        i = 0
        while i < len(ingredientes) and not prohibido_encontrado:
            if ingredientes[i] in prohibidos:
                prohibido_encontrado = True
            i += 1
        if not prohibido_encontrado:
            comidas_permitidas.append(nombre)
    return comidas_permitidas

print(elegir_comidas(comidas_1, prohibidos_1))
print(elegir_comidas(comidas_1,prohibidos_2))
print(elegir_comidas(comidas_1,prohibidos_3))
print(elegir_comidas(comidas_1,prohibidos_4))
print(elegir_comidas(comidas_2,prohibidos_1))
print(elegir_comidas(comidas_2,prohibidos_2))
print(elegir_comidas(comidas_2,prohibidos_3))
print(elegir_comidas(comidas_2,prohibidos_4))

print(doctest.testmod())