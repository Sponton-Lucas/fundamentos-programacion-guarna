
def imprimir_pares_uno(valor1,valor2):
    for i in range(valor1, valor2 + 1):
        if i % 2 == 0:
            print(i)
            
    return

print(imprimir_pares_uno(1, 10))
