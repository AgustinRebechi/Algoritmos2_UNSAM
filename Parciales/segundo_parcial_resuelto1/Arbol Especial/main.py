"""
Se necesita modelar un árbol binario con nodos que se identifican con números enteros que no
se repiten (no está necesariamente ordenado), similar al ArbBin(Entero) que vimos en la
cursada, pero con una particularidad. Este árbol puede tener algunos nodos especiales que,
cuando se realiza un recorrido especial (le diremos recorrido parcial) estos nodos actúan como
si fueran hojas, es decir, como si no tuvieran descendientes. Hay que contemplar que estos
nodos especiales son árboles no vacíos que responden como cualquier otro nodo común en los
recorridos clásicos sobre árboles binarios que hemos visto, por lo cual sólo se diferencian al
momento de hacer un recorrido especial.

Ejemplo:
Nodos especiales: 2 y 7
Recorrido DFS preorder: 3, 2, 1, 5, 6, 7, 0
Recorrido DFS preorder especial: 3. 2. 6. 7

Se solicita realizar lo siguiente:
a) Definir la clase ArbEsp que soporte el modelo propuesto en el enunciado, incluyendo
otras clases adicionales si es necesario. (1 pt)
b) Implementar la operación preorder_especial que, dado un árbol ArbEsp, genere una
lista de enteros con el recorrido preorder especial del árbol, contemplando los
nodos especiales como si fueran hojas. (1 pt)
c) Implementar la operación es_especial que, dado un árbol ArbEsp y un número entero,
devuelva si existe o no en el árbol un nodo especial identificado con ese número. (1 pt)
d) Implementar la operación podados que, dado un árbol ArbEsp, devuelva la cantidad de
nodos del árbol que no se recorren cuando se realiza un recorrido especial, es decir,
la cantidad de nodos que son ignorados en ese tipo de recorrido. (1 pt)

"""
from ArbEsp import ArbEsp

t = ArbEsp.crear_nodo_esp(3)
n2 = ArbEsp.crear_nodo_esp(2,es_especial=True)
n6 = ArbEsp.crear_nodo_esp(6)
n1 = ArbEsp.crear_nodo_esp(1)
n5 = ArbEsp.crear_nodo_esp(5)
n7 = ArbEsp.crear_nodo_esp(7,es_especial=True)
n0 = ArbEsp.crear_nodo_esp(0)

n7.insertar_si(n0)

n6.insertar_sd(n7)

n2.insertar_si(n1)
n2.insertar_sd(n5)

t.insertar_si(n2)
t.insertar_sd(n6)

#B)
print(t.preorder())
print(t.preorder_especial())

#C)
print(t.es_especial(5))
print(t.es_especial(7))

#D)
print(t.podados())