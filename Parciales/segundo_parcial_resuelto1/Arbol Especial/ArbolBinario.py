#Arbol binario generico clasico, usando el arbol vacio

from typing import Generic, Optional, TypeVar, Callable, Any
from functools import wraps

T = TypeVar("T")

class NodoAB(Generic[T]):
    def __init__(self,dato:T ,si: "Optional[ArbolBinario[T]]" = None, sd: "Optional[ArbolBinario[T]]" = None) -> None:
        self.dato = dato
        self.si: ArbolBinario[T] = ArbolBinario() if si is None else si
        self.sd: ArbolBinario[T] = ArbolBinario() if sd is None else sd

    def __str__(self):
        return self.dato


class ArbolBinario(Generic[T]):
    def __init__(self) -> None:
        self.raiz = None


    class Decoradores:
        @classmethod
        def validar_no_es_vacio(cls,f:Callable[...,Any])-> Callable[...,Any]:
            @wraps(f)
            def wrapper(self,*args,**kwargs) -> Any:
                if self.es_vacio():
                    raise TypeError("Arbol Vacio")
                return f(self,*args,*kwargs)
            return wrapper


    


    @staticmethod #Se usa para tener una funcion que podria estar afuera, adentro. Asi empaquetamos. NO LE PASAMOS SELF, eso es para metodos de instancia
    def crear_nodo(dato: T, si: "Optional[ArbolBinario[T]]" = None, sd: "Optional[ArbolBinario[T]]" = None) -> "ArbolBinario[T]":
        t = ArbolBinario()
        t.raiz = NodoAB(dato, si, sd)
        return t
    
    def es_vacio(self) -> bool:
        return self.raiz is None
    
    
    
    @Decoradores.validar_no_es_vacio
    def si(self) -> "ArbolBinario[T]":
        
        return self.raiz.si #type:ignore

    @Decoradores.validar_no_es_vacio
    def sd(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            raise TypeError("Arbol Vacio")
        return self.raiz.sd #type:ignore

    @Decoradores.validar_no_es_vacio
    def dato(self)-> T:
        assert self.raiz is not None
        return self.raiz.dato #type:ignore

    @Decoradores.validar_no_es_vacio
    def insertar_si(self,si:"ArbolBinario[T]"):
        assert self.raiz is not None
        self.raiz.si = si #type:ignore

    @Decoradores.validar_no_es_vacio
    def insertar_sd(self,sd:"ArbolBinario[T]"):
        assert self.raiz is not None
        self.raiz.sd = sd #type:ignore

    def set_raiz(self,nodo : NodoAB[T]):
        self.raiz = nodo

    
    def altura(self)->int:
        if self.es_vacio():
            return 0
        else:
            return 1 + max(self.si().altura(),self.sd().altura())
        
    def __len__(self)->int:
        if self.es_vacio():
            return 0
        else:
            return 1 + len(self.si()) + len(self.sd())



    def preorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return  [self.dato()] + self.si().preorder() + self.sd().preorder() 

    def inorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return   self.si().inorder()+ [self.dato()] + self.sd().indorden() 

    def postorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return   self.si().postorder() + self.sd().postorder() + [self.dato()]  
        
    def preorder_tail(self)->list[T]:
        """Eliminamos la recursion de pila usando una pila explicita."""
        def _bfs(pila: list[ArbolBinario[T]],camino:list[T]) -> list[T]:

            if not pila:
                return camino
            else:
                actual = pila.pop()
                if not actual.es_vacio():    
                    camino.append(actual.dato())
                    pila.append(actual.sd())
                    pila.append(actual.si())
                return _bfs(pila,camino)

        return _bfs([self],[])
    
    def preorder_iter(self) ->list[T]:
        """Eliminamos la recursion de pila usando una pila explicita e iterando. Antes seguia siendo de pila por como funciona python"""
        pila = [self]
        camino = []
        while pila != []:
            actual = pila.pop()
            if not actual.es_vacio():    
                camino.append(actual.dato())
                pila.append(actual.sd())
                pila.append(actual.si())
        return camino




    
    def __str__(self) -> str:
        def recorrer(t: ArbolBinario[T],nivel:int) -> str:
            tab = "_"*4*nivel
            if t.es_vacio():
                return tab + "AV\n"
            else:

                tab += str(t.dato()) + "\n"
                tab += recorrer(t.si(),nivel+1)
                tab += recorrer(t.sd(),nivel+1)
                return tab
        return recorrer(self,0)
    
    def es_hoja(self) -> bool:
        return  not self.es_vacio() and self.si().es_vacio() and self.sd().es_vacio()

    def copy(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            return ArbolBinario()
        else:
            copia = ArbolBinario.crear_nodo(self.dato())
            copia.insertar_si(self.si().copy())
            copia.insertar_sd(self.sd().copy())
            return copia
    

    def bfs(self)->list[T]:
        
        def _bfs(cola: list[ArbolBinario[T]],camino:list[T]) -> list[T]:

            if not cola:
                return camino
            else:
                actual = cola.pop(0)
                if not actual.es_vacio():    
                    camino.append(actual.dato())
                    cola.append(actual.si())
                    cola.append(actual.sd())
                return _bfs(cola,camino)

        return _bfs([self],[])
    
    
        
        
        
    def hojas(self) ->list[T]:
        if self.es_vacio():
            return []
        elif self.es_hoja():
            return [self.dato()]
        else:
            return   self.si().hojas() + self.sd().hojas() 
        
    def sin_hojas(self) -> "ArbolBinario[T]":
        """Devuelvo copia para no hacer lio"""
        if self.es_vacio():
            return ArbolBinario()
        elif self.es_hoja():
            return ArbolBinario()
        else:
            copia = ArbolBinario.crear_nodo(self.dato())
            copia.insertar_si(self.si().sin_hojas())
            copia.insertar_sd(self.sd().sin_hojas())
            return copia
    
    def podar(self,dato:T) -> "ArbolBinario[T]":
        """Esto es post pruning, voy tomando metrica, corto, si no me cambia, sigo."""
        if self.es_vacio() or self.dato() == dato:
            return ArbolBinario()
        else:
            copia = ArbolBinario.crear_nodo(self.dato())
            copia.insertar_si(self.si().podar(dato))
            copia.insertar_sd(self.sd().podar(dato))
            return copia
        
    def espejo(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            return ArbolBinario()
        else:
            copia = ArbolBinario.crear_nodo(self.dato())
            copia.insertar_si(self.sd().espejo())
            copia.insertar_sd(self.si().espejo())
            return copia









if __name__ == "__main__":
    t = ArbolBinario.crear_nodo(1)
    n2 = ArbolBinario.crear_nodo(2)
    n3 = ArbolBinario.crear_nodo(3)
    n4 = ArbolBinario.crear_nodo(4)
    n5 = ArbolBinario.crear_nodo(5)
    n6 = ArbolBinario.crear_nodo(6)
    n7 = ArbolBinario.crear_nodo(7)
    n8 = ArbolBinario.crear_nodo(8)
    n9 = ArbolBinario.crear_nodo(9)
    n10 = ArbolBinario.crear_nodo(10)
    n11 = ArbolBinario.crear_nodo(11)





    t.insertar_si(n2)
    t.insertar_sd(n3)

    n2.insertar_si(n4)
    n2. insertar_sd(n5)

    n4.insertar_si(n8)

    n3.insertar_si(n6)
    n3.insertar_sd(n7)

    n7.insertar_sd(n11)

    n5.insertar_si(n9)
    n5.insertar_sd(n10)


    print(t.hojas())

    t2: ArbolBinario[int] = t.espejo()

    print(t2.preorder())
    print(t2.preorder_tail())
    print(t2.preorder_iter())











