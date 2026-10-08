#Escribir un programa, compuesto por funciones, que permita:
#a) Ingresar en un diccionario, localidades (como clave) y dos datos: cantidad de
#habitantes y cantidad de hospitales públicos (HP). Los datos surgen de distintas
#planillas, por lo que una misma clave (localidad) se puede ingresar varias veces,
#debiendo sumarse los valores.
#b) Listar el total de habitantes y HP para cada localidad.
#c) Imprimir un listado ordenado de mayor a menor de las 5 localidades de mayor
#relación: (habitantes / HP). Indicar la Localidad y la relación resultante.


def validarDatos(localidad, habitantes, hospitales):
    return (habitantes >= 0 and hospitales >= 0 and isinstance(localidad, str) and localidad != "")

def cargarDatos(diccionario, localidad, habitantes, hospitales):
    if localidad in diccionario:
        diccionario[localidad][0] += habitantes
        diccionario[localidad][1] += hospitales
    else:
        diccionario[localidad] = [habitantes, hospitales]
    return diccionario

def ingresoDatos():
    diccionario = {}
    localidad = input("Ingrese la localidad (vacío para salir): ")
    while localidad != "":
        habitantes = int(input("Ingrese la cantidad de habitantes: "))
        hospitales = int(input("Ingrese la cantidad de hospitales públicos: "))
        if validarDatos(localidad, habitantes, hospitales):
            cargarDatos(diccionario, localidad, habitantes, hospitales)
        else:
            print("Datos inválidos. Intente nuevamente.")
        localidad = input("Ingrese la localidad (vacío para salir): ")
    return diccionario

def listarDatos(diccionario):
    print("Listado de localidades con total de habitantes y hospitales públicos:")
    for localidad, datos in diccionario.items():
        print(f"Localidad: {localidad}, Habitantes: {datos[0]}, Hospitales Públicos: {datos[1]}")

def rankingRelaciones(diccionario):
    relaciones = {}
    for localidad, datos in diccionario.items():
        habitantes, hospitales = datos
        if hospitales > 0:
            relacion = habitantes / hospitales
            relaciones[localidad] = relacion
    ranking = sorted(relaciones.items(), key=lambda x: x[1], reverse=True)[:5]
    print("Ranking de localidades por relación habitantes/HP:")
    for localidad, relacion in ranking:
        print(f"Localidad: {localidad}, Relación: {relacion:.2f}")

def main():
    diccionario = ingresoDatos()
    listarDatos(diccionario)
    rankingRelaciones(diccionario)

if __name__ == "__main__":
    main()

