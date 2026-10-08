#Escribir un programa que solicite el ingreso de un texto formado sólo por sustantivos
#en singular, separados uno del otro, por un blanco.
#El usuario ingresará por ejemplo: “casa canción río bebé pez paraguas tórax”
#El programa deberá mostrar cada una de las palabras ingresadas, seguida por su
#palabra en plural, un par por línea (singular - plural), en orden alfabético.
#Validar que las palabras ingresadas por el usuario, sólo contengan letras; caso
#contrario, enviar un mensaje acorde y volver a solicitar el ingreso.
#Las reglas a cumplir para pasar un sustantivo en singular a su plural son:
#a. Agregar una “s” al final, si la palabra termina en vocal sin acento.
#b. Agregar una “s” al final, si la palabra termina con una é (acentuada).
#c. Si la palabra termina en “z”, la reemplazamos por “ces”.
#d. Agregamos “es” al final, si la palabra termina en una consonante (a excepción de la
#“s”, la “z”, y la “x”), ó si la palabra termina con las vocales acentuadas: á, í, ó, ú.
#e. Si el sustantivo termina en “s” ó “x”, consideramos que el plural es igual al
#singular, por lo tanto la función deberá devolver lo mismo que recibió

def pluralizar(palabra):
    """Devuelve el plural de un sustantivo en singular según las reglas dadas."""
    # Regla a: termina en vocal sin acento
    if palabra[-1] in "aeiou" and palabra[-1] not in "áéíóú":
        return palabra + "s"
    # Regla b: termina en é
    elif palabra.endswith("é"):
        return palabra + "s"
    # Regla c: termina en z
    elif palabra.endswith("z"):
        return palabra[:-1] + "ces"
    # Regla d: termina en consonante (excepto s, z, x) o vocal acentuada
    elif palabra[-1] in "bcdfghjklmnpqrtvw" or palabra[-1] in "áíóú":
        return palabra + "es"
    # Regla e: termina en s o x → plural igual al singular
    elif palabra[-1] in "sx":
        return palabra
    else:
        return palabra + "es"


def pedir_palabras():
    """Solicita al usuario palabras válidas (solo letras)."""
    while True:
        texto = input("Ingrese sustantivos en singular separados por espacio: ")
        palabras = texto.split()
        if all(p.isalpha() for p in palabras):
            return palabras
        else:
            print("Error: solo se permiten letras. Intente nuevamente.")


def main():
    palabras = pedir_palabras()
    palabras.sort()  # orden alfabético
    for p in palabras:
        print(f"{p} - {pluralizar(p)}")


if __name__ == "__main__":
    main()
