class Arma:
    def __init__(self, nombre, danio, durabilidad):
        self.nombre = nombre
        self.danio = danio
        self.durabilidad = durabilidad

class Enemigo:
    def __init__(self, nombre, vida, oro):
        self.nombre = nombre
        self.vida = vida
        self.oro = oro

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.oro = 0
    
    def atacar(self, enemigo, arma):
        if arma.durabilidad > 0:
            if enemigo.vida <= 0:
                print(f"No puedes pelear, {enemigo.nombre} ya fue derrotado")
            else:
                enemigo.vida -= arma.danio
                arma.durabilidad -= 1
                print(f"{self.nombre} ataco a {enemigo.nombre}")
                print(f"Danio realizado: {arma.danio}")
                if enemigo.vida > 0:
                    print(f"Vida del enemigo: {enemigo.vida}")
                    print(f"Durabilidad restante: {arma.durabilidad}")
                else:
                    enemigo.vida = 0
                    self.oro += enemigo.oro
                    print(f"{enemigo.nombre} derrotado")
                    print(f"Ganaste {enemigo.oro} de oro")
        else:
            print("El arma esta rota.")


espada = Arma("Espada de Hierro", 20, 4)
dragon = Enemigo("Dragon", 50, 500)
lucas = Jugador("Lucas")

lucas.atacar(dragon, espada)
lucas.atacar(dragon, espada)
lucas.atacar(dragon, espada)
lucas.atacar(dragon, espada)
