# Hacer una funcion en python llamada generar_detalle_infracciones que reciba dos listas y dos valores enteros, y devuelva
# una nueva lista de listas con el detalle de las multas.
#1er lista registros_paso es una lista de listas donde cada elemento representa un vehiculo que paso por el puesto de control.
# [patente, velocidad_registrada] (por ej:[["A123AAA",140],["AB456CO",110]]). La lista fue creada cronologicamente,
#regustrando los vehiculos en el orden exacto en que fueron pasando por el control.
# La segunda lista, patentes_empresa, es una lista que contiene las patentes que pertenecen a la flota oficial de la empresa
#evaluada. Y los dos enteros que debe recibir corresponden al limite_velocidad y a la multa_base.
#La lista de listas a devolver debe contener la patente y el valor de la multa correspondiente, y debe ser generada en el mismo
#orden cronologico en el que ocurrieron las infracciones, y solo de las patentes que corresponden a la empresa. Un mismo vehiculo
# puede tener mas de una infraccion, esto implicaria que apareceria tantas veces como infracciones haya cometido.
#El valor_multa se calcula a partir de la multa_base. Sin embargo, si el vehiculo ya posee una infraccion previa registrada en el
# listado, se le debe aplicar un 10% de recargo adicional a ese valor de multa en particular.
#Si ningun vehiculo de la empresa cometio infracciones, la funcion debe devolver una lista vacia []
# Restricciones: evitar evaluaciones y ciclos innecesarios.Prohibido el uso de los metodos de lista .count(), .index()
# .find(), .sort() o funciones de ordenamiento como sorted().

def generar_detalle_infracciones(registros_paso, patentes_empresa, lim_velocidad, multa_base):
    lista_multas = []
    patentes_infractores = []
    for patente, velocidad_registrada in registros_paso:
        if patente in patentes_empresa and velocidad_registrada >= lim_velocidad:
            if patente in patentes_infractores:
                multa = multa_base * 1.1
            else:
                multa = multa_base
                patentes_infractores.append([patente])
            lista_multas.append([patente, multa])
    return lista_multas