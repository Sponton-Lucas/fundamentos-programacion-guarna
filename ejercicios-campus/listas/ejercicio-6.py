

def es_generala(tupla):
    return len(set(tupla)) == 1

def es_poker(tupla):
    for numero in tupla:
        if tupla.count(numero) == 4:
            return True
    return False

def es_full(tupla):
    for numero in tupla:
        if tupla.count(numero) == 3:
            for otro_numero in tupla:
                if otro_numero != numero and tupla.count(otro_numero) == 2:
                    return True
    return False

#extra con funcion main y ingreso de tupla

def pedir_tupla():
    tupla = []
    for i in range(5):
        while True:
            try:
                numero = int(input(f"Ingrese el número {i + 1} (entre 1 y 6): "))
                if 1 <= numero <= 6:
                    tupla.append(numero)
                    break
                else:
                    print("Número inválido. Debe estar entre 1 y 6.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
    return tuple(tupla)
def main():
    tupla = pedir_tupla()
    if es_generala(tupla):
        print("Es generala")
    elif es_poker(tupla):
        print("Es poker")
    elif es_full(tupla):
        print("Es full")
    else:
        print("No es generala, poker ni full")

main()