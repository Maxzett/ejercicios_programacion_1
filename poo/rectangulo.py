
class Rectangulo:
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    def calcular_area(self) -> str:
        area = self.base * self.altura
        print(f'El area del reactangulo es {area}')
    
    def calcular_perimetro(self) -> str:
        perimetro = self.base * 2 + self.altura * 2
        print(f'El perimetro del rectangulo es {perimetro}')
        
recatangulo_1 = Rectangulo(6, 2)

print(recatangulo_1.calcular_area())
print(recatangulo_1.calcular_perimetro())
        
    