# Mostrar: Curso Python -> Comision 1:2, Comision 2:3, Total curso:5


def main():
    archivo = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-6.csv")
    linea = archivo.readline()
    curso, comision = linea.strip().split(",")
    total_general = 0
    while linea != "":
        curso_actual = curso
        contador_totales = 0
        print(f"\nCurso: {curso_actual}")
        while linea != "" and curso == curso_actual:
            contador = 0
            comision_actual = comision
            while linea != "" and curso == curso_actual and comision == comision_actual:
                contador += 1
                linea = archivo.readline()
                if linea != "":
                    curso, comision = linea.strip().split(",")
            contador_totales += contador
            print(f"Comision {comision_actual}: {contador}")
        print(f"Total curso: {contador_totales}")
        total_general += contador_totales
    print(f"\nTotal general: {total_general}")
    archivo.close()

main()