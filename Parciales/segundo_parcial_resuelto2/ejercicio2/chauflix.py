from usuario import User
from pelicula import Pelicula
from relacion import Relacion

class ChauFlix:
    def __init__(self):
        self.usuarios: dict[str, User] = {}
        self.peliculas: dict[str, Pelicula] = {}
        self.perfiles_similares: list[Relacion] = []
        
    def agregar_usuarix(self, usuario: User):
        if usuario.nombre in self.usuarios:
            raise ValueError(f'Usario {usuario.nombre} ya existe.')
        self.usuarios[usuario.nombre] = usuario
        
    def agregar_pelicula(self, pelicula: Pelicula):
        if pelicula.titulo in self.peliculas:
            raise ValueError(f'Pelicula {pelicula.titulo} ya existe.')
        self.peliculas[pelicula.titulo] = pelicula
        
    def mirar_pelicula(self, user: User, pelicula: Pelicula):
        if user not in self.usuarios.values():
            raise ValueError('Usuario no existe')
        if pelicula not in self.peliculas.values():
            raise ValueError('La pelicula no existe')
        user.ver_pelicula(pelicula)
        self._actualizar_relaciones()

    def get_usuario(self, nombre_usuario: str) -> User:
        return self.usuarios[nombre_usuario]
    
    def get_pelicula(self, titulo_pelicula: str) -> Pelicula:
        return self.peliculas[titulo_pelicula]
    
    def usuarios_similares_a(self, nombre_usuario: str) -> list[User]:
        similares: list[User] = []
        usuario = self.get_usuario(nombre_usuario)
        for otro_usuario in self.usuarios.values():
            if (not (usuario == otro_usuario)) and usuario.es_perfil_similar(otro_usuario):
                similares.append(otro_usuario)
                
        return similares
    
    def _actualizar_relaciones(self):
        self.perfiles_similares = []
        for nombre, usuario in self.usuarios.items():
            for otro_usuario in self.usuarios_similares_a(nombre):
                relacion = Relacion(usuario, otro_usuario)
                if relacion not in self.perfiles_similares:
                    self.perfiles_similares.append(relacion)
                    
    def tienen_relacion(self, user1: User, user2: User) -> bool:
        return user1.es_perfil_similar(user2)
                    
    def tienen_alguna_relacion(self, user1: User, user2: User) -> bool:
        def interna(nombre1, nombre2, visitados: list[str]) -> bool:
            if nombre2 in visitados:
                return False
            visitados.append(nombre2)
            user1 = self.get_usuario(nombre1)
            user2 = self.get_usuario(nombre2)
            if user1.es_perfil_similar(user2):
                return True
            else:
                tiene_relacion = False
                for otro_user in self.usuarios_similares_a(nombre2):
                    tiene_relacion = tiene_relacion or interna(nombre1, otro_user.nombre, visitados)
                return tiene_relacion
        
        return interna(user1.nombre, user2.nombre, [])