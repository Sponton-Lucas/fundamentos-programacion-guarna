
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, monto):
        self.saldo += monto
        print(f"Depositaste {monto} correctamente")
        print(f"Saldo actual: {self.saldo}")
    def extraer(self, monto):
        if monto > self.saldo:
            print("No hay dinero suficiente en la cuenta.")
        else:
            self.saldo -= monto
            print(f"Se extrajo {monto} correctamente.")
            print(f"Saldo en la cuenta: {self.saldo}")

cuenta = CuentaBancaria("Lucas", 1000)

cuenta.depositar(500)
cuenta.extraer(200)
cuenta.extraer(2000)
