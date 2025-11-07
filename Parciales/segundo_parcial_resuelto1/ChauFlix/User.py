from collections import Counter
from Pelicula import Pelicula


class User:
    def __init__(self,name:str) -> None:
        self.name :str = name
        self.perfil :Counter[str,int] = Counter()

    def ver_pelicula(self,pelicula: Pelicula)->None:
        """Modifico su perfil en funcion de los generos de la pelicula vista"""
        for genero in pelicula.generos:
            self.perfil[genero]+=1

    def __repr__(self) -> str:
        return f"{self.name}" 

    def __str__(self) -> str:
        return f"{self.name}: {self.perfil}" 