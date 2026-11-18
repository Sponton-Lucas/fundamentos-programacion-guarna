# Mostrar: Curso: Python -> Comision 1: 2, Comision 2: 2; Curso: Java -> COmision 1:2, Comision 2: 1

def main():
    archivo = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-5.csv")
    linea = archivo.readline()
    curso, comision = linea.strip().split(",")
    while linea != "":
        curso_actual = curso
        print(f"\nCurso: {curso_actual}")
        while linea != "" and curso == curso_actual:
            contador = 0
            comision_actual = comision
            while linea != "" and curso == curso_actual and comision == comision_actual:
                contador += 1
                linea = archivo.readline()
                if linea != "":
                    curso, comision = linea.strip().split(",")
            print(f"Comision {comision_actual}: {contador}")
    archivo.close()

main()