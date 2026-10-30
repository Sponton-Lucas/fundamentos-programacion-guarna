#2) Escribir una funcion en python llamada calcular_peaje_total que reciba dos listas y tres valores enteros, y devuelva el monto
#total acumulado a abonar por una empresa en concepto de peajes de autopista.
# La primera lista, registros_paso, es una lista de listas donde cada elemento representa un vehiculo que paso por el puesto de 
#control con el formato [patente, tipo_vehiculo] (por ej: [["AA123AA","camion"],["AB456CD","auto"]]). Esta lista fue creada
# de manera cronologica, registrando los vehiculos en el orden exacto en que fueron pasando por el control.
# La segunda lista, patentes_empresa, es una lista simple que contiene unicamente las patentes que pertenecen a
# la flota oficial de la empresa evaluada.
# Los tres valores enteros pasados a la funcion son: tarifa_auto, tarifa_moto, tarifa_camion.
# Por un beneficio corporativo, los primeros 9 peajes del dia de la empresa se cobran a tarifa normal. A partir del 10
# peaje inclusive en adelante, la empresa obtiene un 10% de bonificacion sobre la tarifa base de ese vehiculo. Si ningun
# vehiculo de la empresa paso por el puesto de peaje en el dia, la funcion debe devolver 0.
# Restricciones: Evitar evaluaciones y ciclor innecesarios. Prohibido el uso de los metodos de lista .count(), index(),
# .find(), .sort() o funciones de ordenamiento como sorted().

def calcular_peaje_total(registros_paso, patentes_empresa, tarifa_auto, tarifa_moto, tarifa_camion):
    total = 0
    cantidad_empresa = 0
    
    for patente, tipo in registros_paso:
        if patente in patentes_empresa:
            cantidad_empresa += 1
            
            if tipo == "auto":
                tarifa = tarifa_auto
            elif tipo == "moto":
                tarifa = tarifa_moto
            else:
                tarifa = tarifa_camion
            
            if cantidad_empresa >= 10:
                tarifa = tarifa * 0.9
            total += tarifa
    return total