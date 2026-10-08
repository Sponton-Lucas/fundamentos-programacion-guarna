# 1) Escribir una función validar que reciba una cadena de caracteres y devuelva True si una clave contiene
# las restricciones requeridas, False de lo contrario.
#• Debe contener entre 8 y 12 caracteres
#• Debe contener por lo menos un carácter alfabético en mayúsculas (sin acentuar)
#• Debe contener por lo menos un carácter alfabético en minúsculas (sin acentuar)
#• Debe contener por lo menos un dígito numérico
#• Debe contener por lo menos alguno de los siguientes símbolos: [*, -, $, @]
#• Cualquier otro símbolo que no esté en el grupo indicado rechazará la validación


def validar(cadena):
    simbolos = "*-$@"

    if not (8 <= len(cadena) <= 12):
        return False

    hay_mayuscula = False
    hay_minuscula = False
    hay_numero = False
    hay_simbolo = False

    for caracter in cadena:
        if caracter.isupper():
            hay_mayuscula = True
        elif caracter.islower():
            hay_minuscula = True
        elif caracter.isnumeric():
            hay_numero = True
        elif caracter in simbolos:
            hay_simbolo = True
        else:
            # Caracter no permitido
            return False
    return (hay_mayuscula and hay_minuscula and hay_numero and hay_simbolo)
