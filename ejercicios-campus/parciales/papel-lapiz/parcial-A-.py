#2)Escribir una función elegir_comidas en Python que reciba una lista de listas, cada sublista es una comida,
# en donde el primer elemento es el nombre de la comida y los siguientes elementos los respectivos ingredientes.
# También recibe una lista de ingredientes prohibidos. Debe devolver una lista con los nombres de las comidas 
# permitidas (no deben contener ingredientes prohibidos).
#Ejemplo:
#Python
#comidas = [
#    ["milanesa", "bifes de nalga", "pan rallado", "huevo"],
#    ["ravioles", "harina", "espinaca", "ricota"],
#    ["pizza", "queso", "harina", "tomate", "aceitunas"],
#]
#prohibidos_1 = ["huevo", "nueces", "aceitunas"]
#prohibidos_2 = ["huevo", "nueces"]
#elegir_comidas(comidas, prohibidos_1)  # --> ['ravioles']
#elegir_comidas(comidas, prohibidos_2)  # --> ['ravioles', 'pizza']
#Testea la función usando doctest, para 2 listas de comidas de al menos 4 comidas cada una; y 3 listas de ingredientes prohibidos, con al menos 2 ingredientes cada una. Generá 4 casos de prueba diferentes."""



#Ejercicio 3
#Se cuenta con una lista salarios, ya cargada, que contiene sublistas, cada una de esas sublistas tiene los siguientes valores:
# empresa (string), puesto (string), cantidad_de_profesionales (entero), salario_por_profesional (entero en dólares).
#Ejemplo:
#Python
#[["GlobalTek", "Desarrollador", 55, 1800], ["GlobalTek", "Tester", 75, 1300], ["ITSol", "Desarrollador", 44, 1500], ...]
#Se pide que escribas un programa modular (compuesto por funciones) en Python que:
#Procese esa lista y genere un diccionario con clave: puesto y valores: total_cantidad, total_salarios.
# La lista con los valores a procesar se obtiene invocando a la función obtener_lista_salarios() de la librería salarios.
#Luego, debe mostrar por pantalla, los puestos y su promedio salarial, ordenados de mayor a menor por promedios salariales.
# La salida debe estar formateada, de forma que se visualice una columna para los puestos, y otra para el promedio salarial.
