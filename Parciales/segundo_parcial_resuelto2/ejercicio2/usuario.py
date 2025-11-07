from genero import Genero
from pelicula import Pelicula

class User:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.generos: dict = {Genero.ACCION: 0, Genero.COMEDIA: 0, Genero.DRAMA: 0}
        
    def ver_pelicula(self, pelicula: Pelicula):
        for genero in pelicula.generos:
            self.generos[genero] += 1
            
    def es_perfil_similar(self, otro: "User") -> bool:
        similar = True
        for genero in Genero:
            similar = similar and abs(self.generos[genero] - otro.generos[genero]) <= 1
        return similar
    
    def __str__(self) -> str:
        generos = {g.value: v for g, v in self.generos.items()}
        return f'Nombre: {self.nombre}\nGeneros vistos: {generos}'
    
    def __repr__(self) -> str:
        generos = {g.value: v for g, v in self.generos.items()}
        return f'Nombre: {self.nombre} | Generos vistos: {generos}'
    
    def __eq__(self, otro: "User") -> bool:
        return self.nombre == otro.nombre
        