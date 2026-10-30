# Escribir una funcion en python llamada clasificar_alertar_anonimas que reciba dos listas y devuelva dos listas independientes.
# Recibe: La primera lista, historias_clinicas, es una lista de listas donde cada elemento representa la ficha medica de un paciente en el formato:
# [altura, peso, edad] (por ej: [[1.55, 95.0, 62], .....]) Por motivos de confidencialidad y anonimato de los datos, no se incluye ninguna informacion
# como apellidos en los registros. La segunda lista, umbrales_criticos, es una lista simple que contiene unicamente 3 valores de referencia: 
# [altura_minima, peso_maximo, edad_maxima].
# Devuelve: Dos listas independientes, la primera con los indices(posicion en la lista) de los pacientes en alerta_maxima, y la segunda con los indices de los
# pacientes en alerta_preventiva. Para evaluar a cada paciente se deben comprobar los siguientes 3 factores de riesgo de forma independiente:
# (1) Que la altura sea menor a la altura_minima. (2) Que el peso sea mayor al peso_maximo. (3) Que la edad sea mayor a la edad_maxima.
# La funcion debe clasificar a los pacientes con los siguientes criterios, guardando en las listas el numero de indice(posicion 0 , 1 , 2) que ocupan en la lista 
# historias_clinicas. Y se clasifican asi:
# --> alerta_maxima: Si cumple con los 3 factores de riesgo.
# --> alerta_preventiva: Si cumple con 2 de los 3 factores de riesgo.
# Si solo se tiene 1 o ninguno no se incliye en ninguna lista. Si no se encuentran en alguna de las categorias, la funcion debe devolver la lista correspondiente vacia.
# Restricciones: Evitar ciclos y recorridos innecesarios, prohibido el uso de funciones como .count(), .index(), .find(), .sort(), o sorted().

def clasificar_alertas(historias_clinicas, umbrales_criticos):
    alerta_maxima = []
    alerta_preventiva = []
    contador_indice = 0
    
    for altura, peso, edad in historias_clinicas:
        cumplidas = []
        altura_min = umbrales_criticos[0]
        peso_max = umbrales_criticos[1]
        edad_max = umbrales_criticos[2]
        if altura < altura_min:
            cumplidas.append(1)
        if peso > peso_max:
            cumplidas.append(1)
        if edad > edad_max:
            cumplidas.append(1)
        
        if len(cumplidas) == 3:
            alerta_maxima.append(contador_indice)
        elif len(cumplidas) == 2:
            alerta_preventiva.append(contador_indice)
        contador_indice += 1
        cumplidas = []
    return (alerta_maxima, alerta_preventiva)