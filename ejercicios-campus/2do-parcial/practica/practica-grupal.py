def leer(archivo):
    linea = archivo.readline()

    if linea:
        dia,equipo_local,goles_local,equipo_visitante,goles_visitante = linea.strip().split(",")
        dia = int(dia)
        goles_local = int(goles_local)
        goles_visitante = int(goles_visitante)
    else:
        dia = equipo_local = goles_local = equipo_visitante = goles_visitante = None

    return dia, equipo_local, goles_local, equipo_visitante, goles_visitante

def merge(europa, america, resultado):
    dia1, equipo_local1, goles_local1, equipo_visitante1, goles_visitante1 = leer(europa)
    dia2, equipo_local2, goles_local2, equipo_visitante2, goles_visitante2 = leer(america)

    while dia1 != None and dia2 != None:
        if dia1 < dia2:
            resultado.write(f"{dia1},{equipo_local1},{goles_local1}, {equipo_visitante1},{goles_visitante1},europa\n")
            dia1, equipo_local1, goles_local1, equipo_visitante1, goles_visitante1 = leer(europa)
        elif dia1 == dia2:
            resultado.write(f"{dia1},{equipo_local1},{goles_local1}, {equipo_visitante1},{goles_visitante1},europa\n")
            dia1, equipo_local1, goles_local1, equipo_visitante1, goles_visitante1 = leer(europa)
        else:
            resultado.write(f"{dia2},{equipo_local2},{goles_local2}, {equipo_visitante2},{goles_visitante2},america\n")
            dia2, equipo_local2, goles_local2, equipo_visitante2, goles_visitante2 = leer(america)
    while dia1 is not None:
        resultado.write(f"{dia1},{equipo_local1},{goles_local1}, {equipo_visitante1},{goles_visitante1},europa\n")
        dia1, equipo_local1, goles_local1, equipo_visitante1, goles_visitante1 = leer(europa)
    while dia2 is not None:
        resultado.write(f"{dia2},{equipo_local2},{goles_local2}, {equipo_visitante2},{goles_visitante2},america\n")
        dia2, equipo_local2, goles_local2, equipo_visitante2, goles_visitante2 = leer(america)

def main():
    europa = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/europa.csv")
    america = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/america.csv")
    resultado = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/resultado.csv", "w")

    merge(europa, america, resultado)

    europa.close()
    america.close()
    resultado.close()

main()
