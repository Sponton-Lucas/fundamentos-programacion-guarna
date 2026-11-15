

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def describir(self):
        return f"{self.nombre} (${self.precio})"
"""
latte = Producto("Latte", 1500)
medialuna = Producto("Medialuna", 800)

print(latte.describir())
print(medialuna.describir())

latte.precio = 1800

print(latte.describir())
print(medialuna.describir())"""

"""class Cafetera:
    def __init__(self, modelo):
        self.modelo = modelo
        self.agua = 100

cafetera_express = Cafetera("Express")
cafetera_italiana = Cafetera("Italiana")
print(cafetera_express.modelo, cafetera_express.agua)
print(cafetera_italiana.modelo, cafetera_italiana.agua)

cafetera_express.agua = 40
print(cafetera_express.agua, cafetera_italiana.agua)"""

class Cafetera:
    def __init__(self, modelo):
        self.modelo = modelo
        self.agua = 100

    def preparar(self, producto_a_usar):
        if self.agua >= 20:
            self.agua -= 20
            print(f"Preparando: {producto_a_usar.nombre}")
            print(f"Costo: ${producto_a_usar.precio}")
            print(f"Agua restante: {self.agua}%")
        else:
            print("Falta agua.")

mi_maquina = Cafetera("Express")
cafe_latte = Producto("Latte", 1500)
for i in range(6):
    mi_maquina.preparar(cafe_latte)


"""
cafe_latte = Producto("Latte", 1500)
mi_maquina = Cafetera("Express")
mi_maquina.preparar(cafe_latte)"""