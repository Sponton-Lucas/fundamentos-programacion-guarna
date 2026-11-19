# Se dispone de un archivo llamado inscripciones.csv, ordenado por carrera,y dentro de cada carrera por materia
# Cada registro posee: carrera, materia, alumno
# Ej: Ing. Informatica,Algoritmos,Juan; Ing. Informatica,Algoritmos,Ana; Sistemas,Algoritmos,Lucas
# Se pide informar:
# Carrera: Ing. Informatica
# Materia Algoritmos: 2 alumnos
# Materia Matematica: 1 alumno
# Total carrera: 3 alumnos
# Ademas informar la cantidad total de alumnos inscriptos. y carrera con mayor cantidad de alumnos.

def leer(inscripciones):
    linea = inscripciones.readline()
    if linea:
        carrera, materia, alumno = linea.strip().split(",")
    else:
        carrera = materia = alumno = None
    return carrera, materia, alumno

def procesar_archivo(inscripciones):
    carrera, materia, alumno = leer(inscripciones)
    total_carrera = 0
    carrera_max = 0
    carrera_mayor_cant = []
    while carrera != None:
        carrera_actual = carrera
        print(f"Carrera: {carrera_actual}")
        while carrera != None and carrera == carrera_actual:
            cant_materia = 0
            materia_actual = materia
            while carrera != None and carrera == carrera_actual and materia == materia_actual:
                cant_materia += 1
                carrera, materia, alumno = leer(inscripciones)
            total_carrera += cant_materia
            if total_carrera > carrera_max:
                carrera_max = total_carrera
                carrera_mayor_cant = [carrera_actual]
            elif total_carrera == carrera_max:
                carrera_mayor_cant.append(carrera_actual)
            print(f"Materia {materia_actual}: {cant_materia} alumno/s")
    print(f"Total de alumnos inscriptos: {total_carrera}")
    print(f"Carrera/s con mayor cantidad de alumnos:")
    for carre in carrera_mayor_cant:
        print(f"Carrera: {carre}")

def main():
    inscripciones = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-14-inscripciones.csv")
    procesar_archivo(inscripciones)
    inscripciones.close()

main()