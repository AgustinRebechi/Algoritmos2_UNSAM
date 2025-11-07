from User import User
from Pelicula import Pelicula

class ChauFlix:
    def __init__(self) -> None:
        self.usuarios = set()
        self.peliculas = set()
        self.relaciones:dict[str,set] = dict()

    #Controles innecesarios pero por Toc
    def valid_username(self,usuario:User)->None:
        """Si el nombre de usuario ya existe, raise Error"""
        usernames = [user.name for user in self.usuarios]
        if usuario.name in usernames:
            raise ValueError(f"El nombre de usuario {usuario.name} ya esta registrado!")
        
    def valid_pelicula(self,pelicula:Pelicula)->None:
        titulos = [peli.titulo for peli in self.peliculas]
        if pelicula.titulo in titulos:
            raise ValueError(f"La pelicula {pelicula.titulo} ya esta en el catalogo!")
        
    def check_user(self,usuario:User) -> None:
        if usuario not in self.usuarios:
            raise ValueError(f"El usuario {usuario.name} no esta registrado en ChauFlix!")
        
    def check_pelicula(self,pelicula:Pelicula)->None:
        if pelicula not in self.peliculas:
            raise ValueError(f"La pelicula {pelicula.titulo} no esta en el catalogo de ChauFlix :(")

    #Metodos Consigna
    def agregar_usuarix(self,usuario:User)->None:
        self.valid_username(usuario)

        self.usuarios.add(usuario)
        self.relaciones[usuario.name] = set()

    def agregar_pelicula(self,pelicula:Pelicula):
        self.valid_pelicula(pelicula)

        self.peliculas.add(pelicula)

    def mirar_pelicula(self,usuario:User,pelicula:Pelicula) ->None:
        self.check_pelicula(pelicula)
        self.check_user(usuario)

        usuario.ver_pelicula(pelicula)

        self.actualizar_relaciones()

    def actualizar_rel(self,user1:User,user2:User)->None:
        """Actualiza la relacion entre dos usuarios particulares"""
        relacionados = True
        keys = list(set(list(user1.perfil.keys()) + list(user2.perfil.keys())))
        while keys and relacionados:
            key=keys.pop()
            if abs(user1.perfil[key] - user2.perfil[key]) >1:
                relacionados = False
        
        if relacionados:
            self.relaciones[user1.name].add(user2)
            self.relaciones[user2.name].add(user1)
        else:
            if user2 in self.relaciones[user1.name]:
                self.relaciones[user1.name].remove(user2)
            if user1 in self.relaciones[user2.name]:
                self.relaciones[user2.name].remove(user1)
  
                   

    def actualizar_relaciones(self)->None:
        """Actualiza las relaciones entre todos los usuarios"""
        lista_usuarios = list(self.usuarios.copy())
        while lista_usuarios:
            usuario = lista_usuarios.pop()
            for otro in lista_usuarios:
                self.actualizar_rel(usuario,otro)

    
    def tienen_relacion(self,user1:User,user2:User)->bool:
        """Si existe relacion directa entre dos usuarios"""
        return user2 in self.relaciones[user1.name]
    

    def tienen_alguna_relacion_iter(self,user1:User,user2:User) ->bool:
        """Version con iteracion, la hice al principio para ordenar la cabeza"""
        if self.tienen_relacion(user1,user2):
            return True
        
        cola = []
        recorrido = [user1]

        cola+= list(self.relaciones[user1.name])

        relacionados = False
        while cola and not relacionados:
            actual = cola.pop()
            recorrido.append(actual)
            cola+=  [user for user in self.relaciones[actual.name] if user not in recorrido]
            if user2 in self.relaciones[actual.name]:
                relacionados = True
        return relacionados
    

    def tienen_alguna_relacion(self,user1:User,user2:User) -> bool:
        """Version con recursion de cola"""
        if self.tienen_relacion(user1,user2):
            return True
        def interna(cola,recorrido,buscado)->bool:
            if cola:
                actual = cola.pop()
                recorrido.append(actual)
                relacionados = False
                cola += [user for user in self.relaciones[actual.name] if user not in recorrido]
                if buscado in self.relaciones[actual.name]:
                    relacionados = True
                if relacionados:
                    return True
                else:
                    return interna(cola,recorrido,buscado)
            else:
                return False
        return interna([user1],[],user2)

    
    

