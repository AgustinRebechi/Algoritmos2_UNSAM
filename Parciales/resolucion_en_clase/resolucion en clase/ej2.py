from enum import Enum
from collections import Counter

class Genero(Enum):
    ACCION = 'Accion'
    COMEDIA = 'Comedia'
    DRAMA = 'Drama'


class Pelicula:
    def __init__(self, titulo: str, generos: list[Genero], duracion: int) -> None:
        self.titulo = titulo
        self.generos = generos
        self.duracion = duracion


class User:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.perfil = Perfil()

    def __eq__(self, otro: "User") -> bool:
        return isinstance(otro, User) and self.nombre == otro.nombre
    
    def __hash__(self) -> int:
        return self.nombre.__hash__()
    
    def tiene_perfil_similar(self, otro: "User") -> bool:
        return isinstance(otro, User) and self.perfil.es_similar(otro.perfil)
    

class Perfil:
    def __init__(self) -> None:
        self.generos_favoritos = Counter(Genero)    # {ACCION: 0, DRAMA: 0,...}
    
    def actualizar_generos(self, generos: list[Genero]):
        for genero in generos:
            self.generos_favoritos[genero] += 1

    def es_similar(self, otro: "Perfil"):
        if not isinstance(otro, Perfil):
            return False
        
        #for genero in Genero:
        #    if abs(self.generos_favoritos[genero] - otro.generos_favoritos[genero]) > 1:
        #        return False
        # return True
            
        return all(
            [abs(self.generos_favoritos[genero] - otro.generos_favoritos[genero]) <= 1 
             for genero in Genero]
            )



class ChauFlix:
    def __init__(self) -> None:
        self.users: list[User] = []
        self.peliculas: list[Pelicula] = []
        self.relaciones: set[tuple[User, User]] = set()

    def agregar_usuarix(self, user: User):
        if user in self.users:
            raise ValueError('User ya existente')
        self.users.append(user)

    def agregar_pelicula(self, pelicula: Pelicula):
        if pelicula in self.peliculas:
            raise ValueError('Pelicula ya existente')
        self.peliculas.append(pelicula)

    def mirar_pelicula(self, user: User, pelicula: Pelicula):
        user.perfil.actualizar_generos(pelicula.generos)
        self._actualizar_relaciones()

    def _actualizar_relaciones(self):
        self.relaciones = set()
        for i, user1 in enumerate(self.users):
            for user2 in self.users[i+1:]:
                if user1.tiene_perfil_similar(user2):
                    self.relaciones.add((user1, user2))

    def tienen_relacion(self, user1: User, user2: User) -> bool:
        return (user1, user2) in self.relaciones or (user2, user1) in self.relaciones

    def tienen_alguna_relacion(self, user1: User, user2: User) -> bool:
        def recorrer(actual: User, buscado: User, visitados: set[User]) -> bool:
            if not actual in visitados:
                if actual == buscado:
                    return True
                else:
                    visitados.add(actual)
                    for vecino in self.users_conectados(actual):
                        if recorrer(vecino, buscado, visitados):
                            return True
            return False
        
        visitados = set()
        return recorrer(user1, user2, visitados)
                    

    def users_conectados(self, user: User) -> list[User]:
        conectados = []
        for user1, user2 in self.relaciones:
            if user1 == user:
                conectados.append(user2)
            if user2 == user:
                conectados.append(user1)
        return conectados


if __name__ == '__main__':
    chau_flix = ChauFlix()
    # Users
    juana = User("Juana")
    ana = User("Ana")
    maria = User("Maria")
    pedro = User("Pedro")
    chau_flix.agregar_usuarix(juana)
    chau_flix.agregar_usuarix(ana)
    chau_flix.agregar_usuarix(maria)
    chau_flix.agregar_usuarix(pedro)
    # Peliculas
    vengadores = Pelicula("Vengadores", [Genero.ACCION], 180)
    deadpool = Pelicula("Deadpool", [Genero.ACCION, Genero.COMEDIA], 120)
    shawshank = Pelicula("The Shawshank Redemption", [Genero.DRAMA], 142)
    lalaland = Pelicula("La La Land", [Genero.COMEDIA, Genero.DRAMA], 128)
    elpadrino = Pelicula("El Padrino", [Genero.DRAMA], 175)
    chau_flix.agregar_pelicula(vengadores)
    chau_flix.agregar_pelicula(deadpool)
    chau_flix.agregar_pelicula(shawshank)
    chau_flix.agregar_pelicula(lalaland)
    chau_flix.agregar_pelicula(elpadrino)
    # Mirar peliculas: La operación mirar_pelicula() invoca a actualizar_relaciones()
    chau_flix.mirar_pelicula(juana, vengadores)
    chau_flix.mirar_pelicula(juana, vengadores)
    chau_flix.mirar_pelicula(ana, deadpool)
    chau_flix.mirar_pelicula(ana, elpadrino)
    chau_flix.mirar_pelicula(maria, shawshank)
    chau_flix.mirar_pelicula(pedro, lalaland)
    chau_flix.mirar_pelicula(pedro, elpadrino)
    chau_flix.mirar_pelicula(pedro, elpadrino)
    # Relaciones directas
    print(f'Relación directa de Juana con Ana:{chau_flix.tienen_relacion(juana, ana)}') # True
    print(f'Relación directa de Juana con Maria:{chau_flix.tienen_relacion(juana, maria)}') # False
    print(f'Relación directa de Juana con Pedro:{chau_flix.tienen_relacion(juana, pedro)}') # False
    print(f'Relación directa de Ana con Maria:{chau_flix.tienen_relacion(ana, maria)}') # True
    print(f'Relación directa de Ana con Pedro:{chau_flix.tienen_relacion(ana, pedro)}') # False
    print(f'Relación directa de Maria con Pedro:{chau_flix.tienen_relacion(maria, pedro)}') # False
      # Relaciones indirectas
    print(f'Relación alguna de Juana con Ana:{chau_flix.tienen_alguna_relacion(juana, ana)}') # True
    print(f'Relación alguna de Juana con Maria:{chau_flix.tienen_alguna_relacion(juana, maria)}') # True
    print(f'Relación alguna de Juana con Pedro:{chau_flix.tienen_alguna_relacion(juana, pedro)}') # False
    print(f'Relación alguna de Ana con Maria:{chau_flix.tienen_alguna_relacion(ana, maria)}') # True
    print(f'Relación alguna de Ana con Pedro:{chau_flix.tienen_alguna_relacion(ana, pedro)}') # False
    print(f'Relación alguna de Maria con Pedro:{chau_flix.tienen_alguna_relacion(maria, pedro)}') # False