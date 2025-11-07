# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 12:26:41 2025

@author: dpach
"""

from typing import Generic, Optional, TypeVar, List
from collections import deque

T = TypeVar("T")

class Nodo(Generic[T]):
    def __init__(self, dato: T):
        self.dato: T = dato
        self.izquierdo: Optional["Nodo[T]"] = None
        self.derecho: Optional["Nodo[T]"] = None

class ArbolBinario(Generic[T]):
    def __init__(self):
        self.raiz: Optional[Nodo[T]] = None

    def es_vacio(self) -> bool:
        return self.raiz is None

    # Recorridos que devuelven list[T] 

    def preorden(self) -> List[T]:
        """raíz → izquierda → derecha"""
        res: List[T] = []
        def visitar(n: Optional[Nodo[T]]):
            if n is None: return
            res.append(n.dato)          # visita
            visitar(n.izquierdo)
            visitar(n.derecho)
        visitar(self.raiz)
        return res

    def inorden(self) -> List[T]:
        """izquierda → raíz → derecha"""
        res: List[T] = []
        def visitar(n: Optional[Nodo[T]]):
            if n is None: return
            visitar(n.izquierdo)
            res.append(n.dato)          # visita
            visitar(n.derecho)
        visitar(self.raiz)
        return res

    def postorden(self) -> List[T]:
        """izquierda → derecha → raíz"""
        res: List[T] = []
        def visitar(n: Optional[Nodo[T]]):
            if n is None: return
            visitar(n.izquierdo)
            visitar(n.derecho)
            res.append(n.dato)          # visita
        visitar(self.raiz)
        return res

    def por_niveles(self) -> List[T]:
        """BFS: nivel por nivel de izquierda a derecha"""
        res: List[T] = []
        if self.raiz is None:
            return res
        q: deque[Nodo[T]] = deque([self.raiz])
        while q:
            n = q.popleft()
            res.append(n.dato)          # visita
            if n.izquierdo: q.append(n.izquierdo)
            if n.derecho:  q.append(n.derecho)
        return res


# Construimos el árbol:
#         10
#        /  \
#       5    20
#      / \
#     2   7

a = ArbolBinario[int]()
a.raiz = Nodo(10)
a.raiz.izquierdo = Nodo(5)
a.raiz.derecho = Nodo(20)
a.raiz.izquierdo.izquierdo = Nodo(2)
a.raiz.izquierdo.derecho = Nodo(7)

print("Preorden    :", a.preorden())     # [10, 5, 2, 7, 20]
print("Inorden     :", a.inorden())      # [2, 5, 7, 10, 20]
print("Postorden   :", a.postorden())    # [2, 7, 5, 20, 10]
print("Por niveles :", a.por_niveles())  # [10, 5, 20, 2, 7]
