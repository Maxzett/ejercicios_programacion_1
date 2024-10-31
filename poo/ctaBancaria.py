class CuentaBancaria:
    
    def __init__(self, titular: str, saldo: float = 0) -> None:
        self.titular = titular
        self.__saldo = saldo

    def mostrar_saldo(self):
        print(f'Su saldo es de ${self.__saldo}')
    
    def depositar(self, monto: int):
        
        self.__saldo += monto
        print(f'Deposito de ${monto} exitoso.')

    def transferir(self, monto: int):
        self.__saldo -= monto
        print('Transferencia exitosa')
        
cta1 = CuentaBancaria('Pepe', 200)
print(cta1.mostrar_saldo())
print(cta1.depositar(50))
print(cta1.mostrar_saldo())
