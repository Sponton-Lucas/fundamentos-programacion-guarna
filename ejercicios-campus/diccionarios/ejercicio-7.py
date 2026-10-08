#Escribir un programa que permita administrar los datos de una votación electoral.
#Para ello, será necesario que nuestro programa cumpla los siguiente requerimientos:
#a) Gestionar la carga de datos de la votación, almacenando los datos en un
#diccionario de diccionarios, que tendrá el siguiente formato:
#{ provincia: { partido_politico: votos_obtenidos ,,,,,} ,,,,}
#Por cada una de las provincias, tendremos la cantidad de votos obtenidos por cada
#uno de los partidos políticos.
#La carga de datos debe solicitar, la Provincia, el Partido Político, y la cantidad de
#votos. Puede haber más de un ingreso de cantidad de votos, para una misma
#Provincia y Partido Político, en ese caso se deben acumular a los ya existentes.
#La carga finaliza cuando se ingrese como nombre de Provincia, la palabra FIN.
#b) Informar para cada Provincia que Partido obtuvo más votos, indicando la cantidad
#de votos y el porcentaje que representan sobre el total de las votaciones de la
#provincia. El listado debe estar ordenado por el nombre de la Provincia.
#c) Informar el ranking de votos a nivel Nacional por Partido Político. El listado debe
#estar ordenado de mayor a menor por la cantidad de votos obtenidos, y debe figurar
#el Partido Político, la cantidad de votos obtenidos, y el porcentaje respecto del total de
#votos.

def cargarDatos(votoElectoral, provincia, partidoPolitico, votosObtenidos):
    if provincia in votoElectoral:
        if partidoPolitico in votoElectoral[provincia]:
            votoElectoral[provincia][partidoPolitico] += votosObtenidos
        else:
            votoElectoral[provincia][partidoPolitico] = votosObtenidos
    else:
        votoElectoral[provincia] = {partidoPolitico: votosObtenidos}
    return votoElectoral


def solicitarDatos():
    votoElectoral = {}
    provincia = input("Ingrese la Provincia(o 'FIN' para finalizar): ")
    
    while provincia != "FIN":
        partidoPolitico = input("Ingrese el partido politico: ")
        votosObtenidos = int(input("Ingrese los votos obtenidos: "))
        cargarDatos(votoElectoral, provincia, partidoPolitico, votosObtenidos)
        provincia = input("Ingrese la Provincia(o 'FIN' para finalizar): ")
    return votoElectoral


def informarResultados(votoElectoral):
    for provincia in sorted(votoElectoral.keys()):
        totalVotos = sum(votoElectoral[provincia].values())
        partidoGanador = max(votoElectoral[provincia], key=votoElectoral[provincia].get)
        votosGanador = votoElectoral[provincia][partidoGanador]
        porcentajeGanador = (votosGanador / totalVotos) * 100 if totalVotos > 0 else 0
        print(f"Provincia: {provincia}, Partido Ganador: {partidoGanador}, Votos: {votosGanador}, Porcentaje: {porcentajeGanador:.2f}%")

def rankingNacional(votoElectoral):
    ranking = {}
    for provincia in votoElectoral:
        for partido, votos in votoElectoral[provincia].items():
            if partido in ranking:
                ranking[partido] += votos
            else:
                ranking[partido] = votos

    totalVotosNacionales = sum(ranking.values())
    rankingOrdenado = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

    print("\nRanking Nacional por Partido Politico:")
    for partido, votos in rankingOrdenado:
        porcentaje = (votos / totalVotosNacionales) * 100 if totalVotosNacionales > 0 else 0
        print(f"Partido: {partido}, Votos: {votos}, Porcentaje: {porcentaje:.2f}%")

def main():
    diccionario = solicitarDatos()
    informarResultados(diccionario)
    rankingNacional(diccionario)


main()