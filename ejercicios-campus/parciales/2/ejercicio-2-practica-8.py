# Implementar generar_premios_choferes, que reciba por parametros: recorridos, choferes_empresa, km_minimos, premio_base.
# La lista recorridos contiene: [legajo, kilometros], por ej: [[101,150],[205,50],[101,220],[300,180],[205,170]]
# La lista choferes_empresa contiene: [[101,"Carlos"],[205,"Ana"],[400,"Pedro"]] cada elemento tiene [legajo, nombre].
# La funcion debe devolver una nueva lista con [nombre, premio]
#Reglas: Solo participan choferes que figuren en choferes_empresa. Solo generan premio los recorridos cuya cantidad
# de kilometros sea mayor o igual a km_minimos. La primera vez que un chofer obtiene un premio recibe:
# premio_base. Si ese mismo chofer ya obtuvo un premio anteriormente: premio_base * 1.2 (20% extra)
# Debe respetarse el orden cronologico de recorridos.Si ningun chofer obtiene premio, devolver []

def generar_premios_choferes(recorridos, choferes_empresa, km_minimos, premio_base):
    ganadores = []
    gano = []
    
    for legajo_r, kilometros in recorridos:
        for legajo_c, nombre in choferes_empresa:
            if legajo_r == legajo_c and kilometros >= km_minimos:
                if legajo_r in gano:
                    premio = premio_base * 1.2
                else:
                    premio = premio_base
                    gano.append(legajo_r)
                ganadores.append([nombre, premio])
    return ganadores