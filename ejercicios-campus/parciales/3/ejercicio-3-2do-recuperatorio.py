# 3) Crear un programa en python que resuelva el siguiente problema:
# PROCESAMIENTO DE DATOS: Obtener lista de obtener_historias_clinicas() de la libreria gestion_salud.
# Cada elemento de esta lista es una sublista que representa un paciente: (1) diagnostico_principal (ej: ["traumatismo", "resfriado", ...])
# (2) Obra social, (3) Edad. Puede aparecer diagnosticos repetidos.
# Procesar la lista y generar un diccionario llamado catalogo_diagnosticos, donde la clave sea el diagnostico, y los valores:
# cantidad total de pacientes registrados con esa condicion, y promedio de edad de dichos pacientes.
# ANALISIS DE RENDIMIENTO: Informar el o los tipos de diagnosticos con mayor cantidad de pacientes. No se puede ordenar la lista, y la estructura
# de datos solo puede ser recorrida una vez.
# INFORME DE COBERTURAS: Mostrar por pantalla de mayor a menor las coberturas medicas segun la cantidad total de pacientes asociados a cada una. Presentar
# prolijamente en columnas de la manera: Obra social - Cantidad.

from gestion_salud import obtener_historias_clinicas

def generar_diccionario(historias):
    catalogo_diagnosticos = {}
    for diagnostico_principal, obra_social, edad in historia:
        if diagnostico_principal in catalogo_diagnosticos:
            cant_total_registrados = catalogo_diagnosticos[diagnostico_principal][0] + 1
            promedio = (catalogo_diagnosticos[diagnostico_principal][1] + edad) / cant_total_registrados
        else:
            catalogo_diagnosticos[diagnostico_principal] = [1, edad]
    return catalogo_diagnosticos

def analisis_rendimiento(catalogo_diagnosticos):
    mayor = None
    mayor_cant = []
    for diagnostico in catalogo_diagnosticos:
        cant_pacientes = catalogo_diagnosticos[diagnostico][0]
        if mayor == None or cant_pacientes > mayor:
            mayor = cant_pacientes
            mayor_cant = [diagnostico]
        elif cant_pacientes == mayor:
            mayor_cant.append(diagnostico)
    print(" Diagnosticos con mayor cantidad de pacientes")
    for diagnos in mayor_cant:
        print(f"{diagnos} - {mayor}")

def informe_coberturas(historias):
    cobertura_medicas = {}
    for datos in historias:
        obra_social = datos[1]
        if obra_social in cobertura_medicas:
            cobertura_medicas[obra_social][0] +=1
        else:
            cobertura_medicas[obra_social] = [1]
    ordenado = sorted(cobertura_medicas.items(),key=lambda x: x[1][0], reverse=True)
    print("OBRA SOCIAL\t\tCANTIDAD")
    for obra_soc, (cant_pacientes) in ordenado:
        print(f"{obra_social}\t\t- {cant_pacientes[0]}")

def main():
    historias = obtener_historias_clinicas()
    catalogo_diagnosticos = generar_diccionario(historias)
    analisis_rendimiento(catalogo_diagnosticos)
    informe_coberturas(historias)

main()