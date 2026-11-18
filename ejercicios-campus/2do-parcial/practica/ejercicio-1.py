# Realizar un programa que informe: cantidad total de nombres

def main():
    archivo = open("/home/lucaas/Escritorio/facultad/fundamentos-programacion/ejercicios-campus/2do-parcial/practica/ejercicio-1.csv")
    
    linea = archivo.readline()
    cant_nombres = 0
    while linea != "":
        print(linea)
        cant_nombres += 1
        linea = archivo.readline()
    
    archivo.close()
    print("Cantidad total de nombres:", cant_nombres)


main()