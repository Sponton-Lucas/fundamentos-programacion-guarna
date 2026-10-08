# Se cuenta con una lista salarios, ya cargada, que contiene sublistas, cada una de esas sublistas tiene los siguientes
# valores: empresa(string), puesto(string) cantidad_de_profesionales(entera), salario_por_profesional(entero en dolares).
# ejemplo: [["GlobalTek","Dessarrollador",55,1800],["GlobalTek"."Tester",75,1300],["ITSol","Desarrollador",44,1500],...].
# Se pide que escribas un programa modular(compuesto por funciones) en python que:
# 1) procese esa lista y genere un diccionario con clave:puesto y valores: total_cantidad, total_salarios. La lista con 
# los valores a procesar se obtiene invocando a la funcion obtener_lista_salarios() de la libreria salarios.
# 2) Luego, debe mostrar por pantalla, los puestos y su promedio salarial, ordenados de mayor a menor por promedios salariales.
# La salida debe estar formateada, de forma que se visualice una columna para los puestos, y otra para el promedio salarial.

def generar_diccionario(salarios):
    dicc = {}
    for empresa, puesto, cantidad, salario in salarios:
        total_salario = cantidad * salario
        if puesto not in dicc:
            dicc[puesto] = [cantidad, total_salario]
        else:
            dicc[puesto][0] += cantidad
            dicc[puesto][1] += total_salario
    return dicc

def calcular_promedios(dicc):
    lista_promedios = []
    for puesto, (cantidad, total_salarios) in dicc.items():
        promedio = total_salarios / cantidad
        lista_promedios.append((puesto, promedio))
    lista_promedios.sort(key=lambda x: x[1], reverse=True)
    return lista_promedios

def mostrar_promedios(lista_promedios):
    print(f"{'Puesto':<20}{'Promedio Salarial':>20}")
    print("-" * 40)
    for puesto, promedio in lista_promedios:
        print(f"{puesto:<20}{promedio:>20.2f}")

def main():
    salarios = [
    ["GlobalTek","Desarrollador",55,1800],
    ["GlobalTek","Tester",75,1300],
    ["ITSol","Desarrollador",44,1500],
    ["ITSol","Analista",30,2000],
    ["SoftCorp","Tester",40,1200],
    ["SoftCorp","Analista",20,2200]
]

    dicc = generar_diccionario(salarios)
    lista_promedios = calcular_promedios(dicc)
    mostrar_promedios(lista_promedios)

if __name__ == "__main__":
    main()
