# Implementar generar_cargos_estacionamiento, con parametros: ingresos, patentes_abonadas, cargo_base, donde
# ingresos = [["AAA111",8],["BBB222",9],["AAA111",15]] cada elemento representa: [patente, hora]
# Generar una lista [patente, cargo] unicamente para los vehiculos abonados.
# El primer ingreso del dia paga: cargo_base. Si el vehiculo ya habia ingresado antes durante el dia
# cargo_base *1.15 (recargo del 15%)

def generar_cargos_estacionamiento(ingresos, patentes_abonadas, cargo_base):
    cargos_estacionamiento = []
    patente_ingresada = []
    
    for patente, hora in ingresos:
        if patente in patentes_abonadas:
            if patente in patente_ingresada:
                cargo = cargo_base * 1.15
            else:
                cargo = cargo_base
                patente_ingresada.append(patente)
            cargos_estacionamiento.append([patente, cargo])
    return cargos_estacionamiento