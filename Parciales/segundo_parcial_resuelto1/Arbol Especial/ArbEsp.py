from typing import Generic, Optional, TypeVar, Callable, Any
from ArbolBinario import ArbolBinario, T, NodoAB

class NodoABEspecial(Generic[T]):
    """Todos son especiales, pero algunos lo son más que otros..."""
    def __init__(self,dato:T ,si: "Optional[ArbolBinario[T]]" = None, sd: "Optional[ArbolBinario[T]]" = None,es_especial : bool = False) -> None:
        self.dato = dato
        self.si: ArbEsp[int] = ArbEsp() if si is None else si
        self.sd: ArbEsp[int] = ArbEsp() if sd is None else sd
        self.es_especial = es_especial



    def __str__(self):
        return self.dato


class ArbEsp(ArbolBinario[int]):
    @staticmethod #Se usa para tener una funcion que podria estar afuera, adentro. Asi empaquetamos. NO LE PASAMOS SELF, eso es para metodos de instancia
    def crear_nodo_esp(dato: T, si: "Optional[ArbEsp[int]]" = None, sd: "Optional[ArbEsp[int]]" = None, es_especial :bool=False) -> "ArbEsp[int]":
        t = ArbEsp()
        t.raiz = NodoABEspecial(dato, si, sd,es_especial)

        return t
    
    @ArbolBinario.Decoradores.validar_no_es_vacio
    def insertar_si(self,si:"ArbolBinario[T]")->None:
        assert self.raiz is not None
        if self.pertenece(si.dato()):
            raise ValueError("El valor insertado ya pertenece al Arbol!")
        self.raiz.si = si #type:ignore

    @ArbolBinario.Decoradores.validar_no_es_vacio
    def insertar_sd(self,sd:"ArbolBinario[T]")->None:
        assert self.raiz is not None
        if self.pertenece(sd.dato()):
            raise ValueError("El valor insertado ya pertenece al Arbol!")
        self.raiz.sd = sd #type:ignore


    def insertar(self,valor:int,es_especial:bool = False)->None:
        """Quise usarlo para el armado (como no tenia que estar ordenado dije ya fue y lo armo asi).
        Era mas facil para controlar si un nuevo nodo ya pertenecia o no"""
        if not self.pertenece(valor):    
            if self.es_vacio():
                nodo = NodoABEspecial(valor,es_especial=es_especial)
                self.set_raiz(nodo)
            elif valor == self.dato():
                raise ValueError("No se admiten repetidos!")
            
            else:
                if self.altura()%2==0:
                    self.si().insertar(valor,es_especial)
                else:
                    self.sd().insertar(valor,es_especial)
        else:
            raise ValueError("El valor insertado ya pertenece al Arbol!")

    def pertenece(self,valor:int) ->bool:
        """Chequeo de raiz a hojas si el valor esta o no en el arbol"""
        if not self.es_vacio():
            if self.dato()==valor:
                return True
            else:
                if self.es_hoja():
                    return False
                return self.si().pertenece(valor) or self.sd().pertenece(valor)
        else:
            return False
        
    def raiz_especial(self) -> bool:
        return self.raiz.es_especial
        
    def preorder_especial_iter(self) -> list[int]:
        """No decia que tenia que ser recursivo :)"""
        pila = [self]
        camino = []
        while pila != []:
            actual = pila.pop()
            if not actual.es_vacio():
                camino.append(actual.dato())

                if not actual.raiz_especial():
                    pila.append(actual.sd())
                    pila.append(actual.si())
        return camino
    
    def preorder_especial(self) ->list[int]:
        """Lo arme recursivo al final porque me daba cosa entregar el iterado jajaja"""
        def interna(pila: list[ArbEsp],camino:list[int]) -> list[int]:

            if not pila:
                return camino
            else:
                actual = pila.pop()
                if not actual.es_vacio():    
                    camino.append(actual.dato())
                    if not actual.raiz_especial():
                        pila.append(actual.sd())
                        pila.append(actual.si())
                return interna(pila,camino)

        return interna([self],[])
    

    def es_especial(self,valor:int) -> bool:
        """True si hay un nodo especial en el arbol que tenga ese valor, sino no. """
        if not self.pertenece(valor):
            raise ValueError("El valor ingresado no pertenece al arbol")
        def interna(arbol) ->bool:
            if arbol.es_vacio():
                return False       
            elif arbol.dato() == valor:
                return arbol.raiz_especial()
            else:
                if not arbol.es_hoja():
                    return interna(arbol.si()) or interna(arbol.sd())
                else:
                    return False
        return interna(self)
        
    def podados(self):
        def recorrido_normal(arbol:ArbEsp)->list[int]:
            if arbol.es_vacio():
                return []
            elif arbol.es_hoja():
                return []
            if arbol.raiz_especial():
                return recorrido_especial(arbol.si()) + recorrido_especial(arbol.sd())
            return recorrido_normal(arbol.si()) + recorrido_normal(arbol.sd())


        def recorrido_especial(arbol:ArbEsp)->list[int]:
            if arbol.es_vacio():
                return []
            elif arbol.es_hoja():
                return [arbol.dato()]
            else:
                return [arbol.dato()] + recorrido_especial(arbol.si()) + recorrido_especial(arbol.sd())

        return recorrido_normal(self)








 

    
    
        
        











