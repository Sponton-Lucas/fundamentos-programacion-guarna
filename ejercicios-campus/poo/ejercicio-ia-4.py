
class Arma:
    def __init__(self, nombre, danio):
        self.nombre = nombre
        self.danio = danio


class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
    
    def atacar(self, enemigo, arma):
        enemigo.vida -= arma.danio
        if enemigo.vida < 0:
            enemigo.vida = 0
        
        print(f"{self.nombre} ataco a {enemigo.nombre} con {arma.nombre}")
        print(f"{enemigo.nombre} recibio {arma.danio} de danio")
        print(f"Vida restante: {enemigo.vida}")

espada = Arma("Espada", 15)

goku = Personaje("Goku")
vegeta = Personaje("Vegeta")

goku.atacar(vegeta, espada)