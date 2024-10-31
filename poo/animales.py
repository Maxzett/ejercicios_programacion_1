class Animal:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre


class Perro(Animal):

    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)
        
    def ladrar(self) -> str:
        print(f'{self.nombre} esta ladrando: "guau guau"')
    

class Gato(Animal):
    
    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)

    def maushar(self) -> str:
        print(f'{self.nombre} esta maushando: "miau miau"')

perrito = Perro('otto')
print(perrito.ladrar())

gatito = Gato('michi')
print(gatito.maushar())
