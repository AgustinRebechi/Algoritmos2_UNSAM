from genero import Genero

class Pelicula:
    def __init__(self, titulo: str, generos: list[Genero], duracion: int,):
        self._titulo = titulo
        self._duracion = duracion
        self._generos = generos
        
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def duracion(self):
        return self._duracion
    
    @property
    def generos(self):
        return self._generos.copy()
        
    def __str__(self) -> str:
        gen = [g.value for g in self.generos]
        return f'Titulo: {self.titulo}\nGeneros: {gen}'