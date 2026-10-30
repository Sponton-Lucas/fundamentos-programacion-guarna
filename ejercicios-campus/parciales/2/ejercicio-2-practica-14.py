# Escribir una funcion elegir_hotel en python para decidir si se reserva o no una estadia en un hotel. La funcion debe devolver True si el hotel es aceptado
# y False en caso contrario.
# La funcion recibe dos listas y un entero: servicios_hotel: servicios_ofrecidos por el hotel, servicios_deseados: servicios que busca el cliente,
# precio_noche: costo por noche.
# El hotel sera aceptado si: Ofrece al menos 3 servicios deseados, el precio por noche es menor o igual a PRECIO_MAXIMO(suponer constante predefinida)
# Ej: lsita_1 = ["wifi","pileta","desayuno","gimnasio","spa"]
# lista_2 = ["wifi","pileta","desayuno"]
# lista_3 = ["wifi","estacionamiento","masajes"]
# elegir_hotel(lista_1,lista_2,12000)
# --> True si 12000 <= PRECIO_MAXIMO

def elegir_hotel(servicios_hotel, servicios_deseados, precio_noche):
    servicios_encontrado = []
    for servicio in servicios_deseados:
        if servicio in servicios_hotel:
            servicios_encontrado.append(servicio)
    return (len(servicios_encontrado) >= 3 and precio_noche <= PRECIO_MAXIMO)