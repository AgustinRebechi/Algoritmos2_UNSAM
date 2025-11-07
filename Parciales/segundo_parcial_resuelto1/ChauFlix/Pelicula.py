

class Pelicula:
    def __init__(self,titulo:str,generos:list[str], duracion:int) -> None:
        self.titulo:str = titulo
        self.duracion:int = duracion
        self.generos = generos

    def __repr__(self) -> str:
        return f"{self.titulo} ({self.duracion}): {self.generos}"

    def __str__(self) -> str:
        return f"{self.titulo} ({self.duracion}): {self.generos}"