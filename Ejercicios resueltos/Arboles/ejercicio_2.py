# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 11:23:01 2025

@author: dpach
"""

# Implementar la operación __eq__() para un árbol que permita identificar si dos árboles son iguales.

# Agregar método especial __eq__
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def es_vacio(self):
        return self.raiz is None

    def __eq__(self, other):
        if not isinstance(other, ArbolBinario):
            return NotImplemented
        # Compara recursivamente las raíces
        def iguales(n1, n2):
            # si ambos vacíos, son iguales
            if n1 is None and n2 is None:
                return True
            # Uno vacío y el otro no, son  distintos
            if n1 is None or n2 is None:
                return False
            # Mismo dato y subárboles izquierdo/derecho iguales
            return (
                n1.dato == n2.dato and
                iguales(n1.izquierdo, n2.izquierdo) and
                iguales(n1.derecho, n2.derecho)
            )

        return iguales(self.raiz, other.raiz)

# Implementación, creamos 2 árboles iguales

# Árbol A
a = ArbolBinario()
a.raiz = Nodo(10)
a.raiz.izquierdo = Nodo(5)
a.raiz.derecho = Nodo(20)
a.raiz.izquierdo.izquierdo = Nodo(2)
a.raiz.izquierdo.derecho = Nodo(7)

# Árbol B (misma forma y valores)
b = ArbolBinario()
b.raiz = Nodo(10)
b.raiz.izquierdo = Nodo(5)
b.raiz.derecho = Nodo(20)
b.raiz.izquierdo.izquierdo = Nodo(2)
b.raiz.izquierdo.derecho = Nodo(7)

# Árbol C (forma distinta)
c = ArbolBinario()
c.raiz = Nodo(10)
c.raiz.izquierdo = Nodo(5)
c.raiz.derecho = Nodo(20)
c.raiz.derecho.izquierdo = Nodo(2)   # cambiado de lugar
c.raiz.derecho.derecho = Nodo(7)

print(a == b)  # True  (idénticos)
print(a == c)  # False (forma distinta)
