class CuentaDeAhorros:
    
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Deposito de {cantidad} completado. Saldo actual: {self._saldo} USD.")
        else:
            print("Cantidad inválida para depósito.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Retiro de {cantidad} completado. Saldo actual: {self._saldo} USD.")
        else:
            print("Cantidad inválida para retiro o fondos insuficientes.")

    def consultar_saldo(self):
        print(f"Saldo actual: {self._saldo} USD.")

cuenta = CuentaDeAhorros(1000)  
cuenta.consultar_saldo()  
cuenta.depositar(500)     
cuenta.consultar_saldo()  
cuenta.retirar(200)     
cuenta.consultar_saldo()  