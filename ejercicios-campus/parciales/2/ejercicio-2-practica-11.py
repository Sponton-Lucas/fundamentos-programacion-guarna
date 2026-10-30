# Escribir una funcion generar_aprobados(examenes, nota_minima) que recibe: una lista de listas examenes, una nota minima
# para aprobar. Cada elemento de examenes tiene la forma: [nombre_alumno, nota]. Por ej: [["Ana",8],["Juan",7],["Pedro",5],["Ana",6]]
# La funcion debe devolver una lista con los nombres de los alumnos que obtuvieron una nota mayor o igual a la nota minima.
# Cada alumno debe aparecer una sola vez en la lista resultado, aunque tenga varios examenes aprobados.
# Por ej: >>> generar_aprobados(examenes,6) --> ["Ana","Pedro"]