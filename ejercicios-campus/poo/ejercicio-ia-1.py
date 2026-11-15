
class Videojuego:
    def __init__(self, titulo, horas_jugadas):
        self.titulo = titulo
        self.horas_jugadas = horas_jugadas
        
    def jugar(self, horas_juego):
        self.horas_jugadas += horas_juego
        print(f"{self.titulo}: {self.horas_jugadas} horas jugadas")

elden_ring = Videojuego("Elden Ring", 1)

elden_ring.jugar(3)
elden_ring.jugar(2)

print(elden_ring.horas_jugadas)
