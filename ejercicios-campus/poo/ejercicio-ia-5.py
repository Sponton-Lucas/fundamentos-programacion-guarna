class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = 0
    
    def vender(self, producto, cantidad):
        if producto.stock >= cantidad:
            producto.stock -= cantidad
            self.dinero += producto.precio * cantidad
            print(f"Se vendieron {cantidad} {producto.nombre}")
            print(f"Dinero en caja: ${self.dinero}")
            print(f"Stock restante: {producto.stock}")
        else:
            print("No hay suficiente stock.")

coca = Producto("Coca-Cola", 1500, 10)

kiosco = Tienda("Kiosco Lucas")
kiosco.vender(coca,3)
kiosco.vender(coca, 5)
kiosco.vender(coca, 4)