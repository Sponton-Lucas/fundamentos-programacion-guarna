#Necesitamos elegir al azar una persona, dentro de un grupo de personas. Por ello
#escribiremos un programa que nos permita realizar esta operación.
#El programa deberá solicitar el ingreso de los nombres y apellidos de cada uno de los
#integrantes de este grupo. El ingreso de nombres finalizará cuando el usuario en lugar
#de ingresar un nombre y apellido, simplemente, de enter.
#A medida que se ingresan los nombres y apellidos, se debe controlar que el que se
#está ingresando, no haya sido ingresado.
#Una vez finalizada la carga, el programa deberá informar cual es el elegido.
import random
def pedir_persona():
    personas = []
    valido = True
    while valido:
        nombre = input(("Ingrese el nombre y apellido de la persona (o presione Enter para finalizar): "))
        if nombre == "":
            valido = False
        elif nombre.lower() in personas:
            print("La persona ya ha sido ingresada.")
        else:
            personas.append(nombre.lower())
    return personas

def main():
    personas = pedir_persona()
    if personas:
        elegido = random.choice(personas)
        print(f"La persona elegida es: {elegido}")
    else:
        print("No se ingresaron personas.")

main()