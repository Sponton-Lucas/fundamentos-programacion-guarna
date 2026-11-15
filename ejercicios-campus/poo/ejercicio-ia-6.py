class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 100

    def usar_pocion(self, pocion):
            energia_antes = self.energia
            self.energia += pocion.recuperacion
            if self.energia > 100:
                self.energia = 100
            energia_recuperada = self.energia - energia_antes
            print(f"{self.nombre} uso {pocion.nombre}")
            print(f"Recupero {energia_recuperada} de energia")
            print(f"Energia actual: {self.energia}")

class Pocion:
    def __init__(self, nombre, recuperacion):
        self.nombre = nombre
        self.recuperacion = recuperacion

mate = Pocion("Mate", 20)
lucas = Jugador("Lucas")
lucas.energia = 60
lucas.usar_pocion(mate)