# Informar cantidad de personas y el promedio de edad

def main():
    archivo = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-2.csv")
    
    linea = archivo.readline()
    cant_personas = 0
    total_edades = 0
    while linea != "":
        persona, edad = linea.strip().split(",")
        print(linea)
        cant_personas += 1
        total_edades += int(edad)
        linea = archivo.readline()
    promedio = total_edades / cant_personas
    print(cant_personas)
    print(total_edades)
    print(promedio)
    archivo.close()

main()