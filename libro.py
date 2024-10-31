class Libro:
    def __init__(self, id: int, titulo: str, autor: str, año: int) -> None:
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def retornar_datos_libro(self) -> str:
        print(f"Este libro es {self.titulo} de {self.autor}, se publico en {self.año}")


libro_1 = Libro(1, 'Harry Potter', 'JK Rowling', 2002)

print(libro_1.retornar_datos_libro())


