from usuario import User
from enum import Enum

class Relacion:
    def __init__(self, usuario1: User, usuario2: User):
        self.usuario1 = usuario1
        self.usuario2 = usuario2
        
    def __eq__(self, otro: "Relacion") -> bool:
        a = self.usuario1 == otro.usuario1 and self.usuario2 == otro.usuario2
        b = self.usuario1 == otro.usuario2 and self.usuario2 == otro.usuario1
        return a or b
    
    def __str__(self) -> str:
        return f'({self.usuario1.nombre}, {self.usuario2.nombre})'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __contains__(self, item: User) -> bool:
        return item == self.usuario1 or item == self.usuario2