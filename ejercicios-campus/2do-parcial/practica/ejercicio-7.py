# Mostrar: Curso Python -> Comision 1:2, Comision 2: 2, Trabajan en Python: 3

def main():
    archivo = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-7.csv")
    linea = archivo.readline()
    if linea != "":
        curso, comision, trabajan = linea.strip().split(",")
    while linea != "":
        curso_actual = curso
        cant_trabajan = 0
        print(f"\nCurso: {curso_actual}")
        while linea != "" and curso == curso_actual:
            contador = 0
            comision_actual = comision
            while linea != "" and curso == curso_actual and comision == comision_actual:
                contador += 1
                if trabajan == "SI":
                    cant_trabajan +=1
                linea = archivo.readline()
                if linea != "":
                    curso, comision, trabajan = linea.strip().split(",")
            print(f"Comision {comision_actual}: {contador}")
        print(f"Trabajan en {curso_actual}: {cant_trabajan}")
    archivo.close()

main()