# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 11:37:24 2025

@author: dpach
"""

"""
Implementar una función recursiva que, dado un árbol binario y una lista de instrucciones ('izquierda' o 'derecha') 
que conforma un camino guiado comenzando desde el nodo raíz, devuelva el contenido del nodo 
que sea accesible utilizando el camino guiado.
"""


from typing import Optional, List, Any

class Nodo:
    def __init__(self, dato: Any):
        self.dato = dato
        self.izquierdo: Optional['Nodo'] = None # puede ser Nodo o None
        self.derecho: Optional['Nodo'] = None

class ArbolBinario:
    def __init__(self):
        self.raiz: Optional[Nodo] = None

    def es_vacio(self) -> bool:
        return self.raiz is None

    def contenido_en_camino(self, camino: List[str]) -> Optional[Any]:
        """Devuelve el dato del nodo alcanzado siguiendo el camino desde la raíz.
           Si el camino no es válido (falta nodo), devuelve None.
        """
        def normalizar(palabra: str) -> str:
            p = palabra.strip().lower()
            # Acepta variantes comunes
            if p in ("izq", "i", "left"): return "izquierda"
            if p in ("der", "d", "right"): return "derecha"
            return p

        def ir(nodo: Optional[Nodo], instrucciones: List[str]) -> Optional[Any]:
                                        # lista de indicaciones
            # Caso 1: no hay nodo -> camino inválido
            if nodo is None:
                return None
            # Caso base: sin instrucciones -> estamos en el nodo destino
            if not instrucciones:
                return nodo.dato
            # Tomo la primera instrucción y sigo recursivamente
            paso = normalizar(instrucciones[0])
            resto = instrucciones[1:]
            if paso == "izquierda":
                return ir(nodo.izquierdo, resto)
            elif paso == "derecha":
                return ir(nodo.derecho, resto)
            else:
                # instrucción desconocida → camino inválido
                return None

        return ir(self.raiz, camino)

# Armamos el arbolito del ejemplo:
#         10
#        /  \
#       5    20
#      / \
#     2   7

a = ArbolBinario()
a.raiz = Nodo(10)
a.raiz.izquierdo = Nodo(5)
a.raiz.derecho = Nodo(20)
a.raiz.izquierdo.izquierdo = Nodo(2)
a.raiz.izquierdo.derecho = Nodo(7)

print(a.contenido_en_camino(["izquierda"]))                  # 5
print(a.contenido_en_camino(["izquierda", "derecha"]))       # 7
print(a.contenido_en_camino(["izquierda", "izquierda"]))     # 2
print(a.contenido_en_camino(["derecha"]))                    # 20
print(a.contenido_en_camino(["derecha", "izquierda"]))       # None  (no hay ese nodo)
print(a.contenido_en_camino(["i", "der"]))                   # 7     (acepta abreviaturas)





