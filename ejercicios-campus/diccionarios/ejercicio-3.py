#Dado el diccionario "dic_materias" que tiene cargados los nombre de las materias
#como clave, y como valor asociado, una lista con tres números enteros, que indican:
#la cantidad de alumnos anotados (como primer valor), cantidad de alumnos que
#rindieron el parcial (segundo valor), cantidad de alumnos que aprobaron el parcial
#(tercer valor).
#Se pide que escribas:
#a) Una función que reciba el diccionario y devuelva una lista con las materias cuyo
#índice de deserción sea mayor al 50% (esto se calcula teniendo en cuenta la cantidad
#de alumnos que rindieron el parcial sobre la cantidad de anotados).
#b) Una función que reciba el diccionario y que devuelva una lista de tuplas, formadas
#por pares (materia, porcentaje_aprobados), ordenada de mayor a menor por
#porcentaje de aprobados (en este caso, se calcula sobre la cantidad que rindieron)

diccionario_materias = {"Matematica": [10, 4, 2], "Ingles": [21, 10, 1], "Fisica": [13, 9, 7]}

def desercionMateria(dic_materias):
    materiasDesercion = []
    for materia, (anotados, rindieron, aprobaron) in dic_materias.items():
        if anotados > 0 and rindieron * 2 < anotados:
            materiasDesercion.append(materia)
    return materiasDesercion
resultadoDesertores = desercionMateria(diccionario_materias)
print(resultadoDesertores)

def porcentajeAprobados(dic_materias):
    aprobados = []
    for materia, (anotados, rindieron, aprobaron) in dic_materias.items():
        if rindieron > 0:
            porcentaje = int(aprobaron * 100 / rindieron)
            aprobados.append((materia, porcentaje))
    return sorted(aprobados, key=lambda tupl: tupl[1], reverse=True)

resultadoPorcentaje = porcentajeAprobados(diccionario_materias)
print(resultadoPorcentaje)