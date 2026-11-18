# Mostrar: Python -> 3, Java -> 2, Testing -> 4

def main():
    archivo = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-4.csv")
    curso = archivo.readline()
    while curso != "":
        curso_actual = curso
        contador = 0
        while curso != "" and curso == curso_actual:
            contador += 1
            curso = archivo.readline()
        print(f"{curso_actual.strip()} -> {contador}")
    archivo.close()
main()