from ChauFlix import ChauFlix
from Pelicula import Pelicula
from User import User
from Genero import Genero


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

# print(chau_flix.usuarios)
# print(chau_flix.peliculas)
# print(chau_flix.relaciones)

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

# print(chau_flix.peliculas)

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