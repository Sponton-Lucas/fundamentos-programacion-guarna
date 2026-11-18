# Informar el nombre de la persona con mayor edad y la edad maxima

def main():
    archivo = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-2.csv")
    linea = archivo.readline()
    max_edad = 0
    persona_mayor = "Nadie"
    while linea != "":
        persona, edad = linea.strip().split(",")
        if int(edad) > max_edad:
            max_edad = int(edad)
            persona_mayor = persona
        linea = archivo.readline()
    print("Persona con la mayor edad:")
    print(f"{persona_mayor} - {max_edad}")
    archivo.close()


main()