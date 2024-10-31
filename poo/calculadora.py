class Calculadora:
    
    def __init__(self, num_1: int, num_2: int) -> None:
        self.num_1 = num_1
        self.num_2 = num_2

    def sumar(self):
        resultado = self.num_1 + self.num_2
        print(f'La suma da {resultado}')

    def restar(self):
        resultado = self.num_1 - self.num_2
        print(f'La resta da {resultado}')

    def multiplicar(self):
        resultado = self.num_1 * self.num_2
        print(f'El resultado de la multiplicacion es {resultado}')

    def dividir(self):
        resultado = self.num_1 / self.num_2
        print(f'El resultado de la division es {resultado}')


calculo_1 = Calculadora(50, 8)

print(calculo_1.sumar())
print(calculo_1.restar())
print(calculo_1.multiplicar())
print(calculo_1.dividir())