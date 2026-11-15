
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
    
    def mostrar_estado(self):
        print(f"{self.nombre} tiene {self.vida} de vida")
    
    def recibir_danio(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nombre} recibio {cantidad} de danio")

goku = Personaje("Goku")

goku.mostrar_estado()
goku.recibir_danio(30)
goku.mostrar_estado()
goku.recibir_danio(90)
goku.mostrar_estado()