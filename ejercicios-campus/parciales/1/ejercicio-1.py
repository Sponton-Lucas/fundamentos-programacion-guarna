# Escribir una funcion que reciba una cadena de caracteres que representa un alias bancario.
# la funcion debe devolver True o False, en base a haber evaluado que dicho alias este bien formado.
#se debe controlar:
#a) que tenga entre 8 y 20 caracteres, pudiendo ser letras, numeros y caracteres especiales(guion del medio, guion bajo o punto)
#b) que contenga al menos 6 letras y un caracter especial
#c) que los caracteres especiales no se encuentren ni en la primera ni la ultima posicion
# Restriccion: de los metodos de la clase cadena, solo se puede usar el metodo isalpha. Se debe evitar ciclos innecesarios.

def validar_alias(alias):
    # Verificar la longitud del alias
    if len(alias) < 8 or len(alias) > 20:
        return False
    
    # Contar letras y caracteres especiales
    letras = sum(1 for caracter in alias if caracter.isalpha())
    especiales = sum(1 for caracter in alias if caracter in "-_.")
    
    # Verificar que haya al menos 6 letras y al menos 1 caracter especial
    if letras < 6 or especiales < 1:
        return False
    if not all(c.isalpha() or c.isdigit() or c in "-_." for c in alias):
        return False

    
    # Verificar que los caracteres especiales no esten en la primera ni ultima posicion
    if alias[0] in "-_." or alias[-1] in "-_.":
        return False
    
    return True


print(validar_alias("user-name"))  # Ejemplo de uso
print(validar_alias("user_name."))  # Ejemplo de uso
print(validar_alias("username"))  # Ejemplo de uso
print(validar_alias("user67.name"))  # Ejemplo de uso

#version con while sin expresion generadora:

def validar_alias(alias):
    # Verificar longitud
    if len(alias) < 8 or len(alias) > 20:
        return False

    letras = 0
    especiales = 0
    i = 0

    while i < len(alias):
        c = alias[i]

        # Validar que el carácter sea permitido
        if not (c.isalpha() or c.isdigit() or c in "-_."):
            return False

        # Contar letras y especiales
        if c.isalpha():
            letras += 1
        elif c in "-_.":
            especiales += 1

        i += 1

    # Verificar reglas adicionales
    if letras < 6 or especiales < 1:
        return False
    if alias[0] in "-_." or alias[-1] in "-_.":
        return False

    return True
