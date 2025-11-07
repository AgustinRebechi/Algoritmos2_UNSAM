from typing import Any, Generic, Optional, TypeVar
from functools import wraps
from collections.abc import Callable

T = TypeVar('T')

class NodoAB(Generic[T]):
    def __init__(self, dato: T, si: "Optional[ArbolBinario[T]]" = None, sd: "Optional[ArbolBinario[T]]" = None):
        self.dato = dato
        self.si: ArbolBinario[T] = ArbolBinario() if si is None else si
        self.sd: ArbolBinario[T] = ArbolBinario() if sd is None else sd

    def __str__(self) -> str:
        return str(self.dato)

class ArbolBinario(Generic[T]):
    def __init__(self):
        self.raiz: Optional[NodoAB[T]] = None
        
    class _Decoradores:
        @classmethod
        def valida_es_vacio(cls, f: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(f)
            def wrapper(self, *args: Any, **kwargs: Any) -> Any:
                if self.es_vacio():
                    raise TypeError('Arbol Vacio')
                return f(self, *args, **kwargs)
            return wrapper
        
    @staticmethod
    def crear_nodo(dato: T, si: "Optional[ArbolBinario[T]]" = None, sd: "Optional[ArbolBinario[T]]" = None) -> "ArbolBinario[T]":
        t = ArbolBinario()
        t.raiz = NodoAB(dato, si, sd)
        return t

    def es_vacio(self) -> bool:
        return self.raiz is None
    
    @_Decoradores.valida_es_vacio
    def si(self) -> "ArbolBinario[T]":
        assert self.raiz is not None
        return self.raiz.si
    
    @_Decoradores.valida_es_vacio
    def sd(self) -> "ArbolBinario[T]":
        assert self.raiz is not None
        return self.raiz.sd
    
    def es_hoja(self) -> bool:
        return not self.es_vacio() and self.si().es_vacio() and self.sd().es_vacio()

    @_Decoradores.valida_es_vacio
    def dato(self) -> T:
        assert self.raiz is not None
        return self.raiz.dato
    
    @_Decoradores.valida_es_vacio
    def insertar_si(self, si: "ArbolBinario[T]"):
        assert self.raiz is not None
        self.raiz.si = si

    @_Decoradores.valida_es_vacio
    def insertar_sd(self, sd: "ArbolBinario[T]"):
        assert self.raiz is not None
        self.raiz.sd = sd
        
    def copy(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            return ArbolBinario()
        nuevo = ArbolBinario.crear_nodo(self.dato())
        nuevo.insertar_sd(self.sd().copy())
        nuevo.insertar_si(self.si().copy())
        return nuevo
    
    def existe(self, val: T) -> bool:
        if self.es_vacio():
            return False
        if self.dato() == val:
            return True
        else:
            return self.si().existe(val) or self.sd().existe(val)
        
    def preorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return [self.dato()] + self.si().preorder() + self.sd().preorder()
        
    def __len__(self) -> int:
        if self.es_vacio():
            return 0
        else:
            return 1 + len(self.si()) + len(self.sd())
    
    def __str__(self):
        def mostrar(t: ArbolBinario[T], nivel: int):
            tab = '.' * 4
            indent = tab * nivel
            if t.es_vacio():
                return indent + 'AV\n'
            else:
                out = indent + str(t.dato()) + '\n'
                out += mostrar(t.si(), nivel + 1)
                out += mostrar(t.sd(), nivel + 1)
                return out
            
        return mostrar(self, 0)
    
class ArbEsp(ArbolBinario[int]):
    def __init__(self, es_especial: bool):
        super().__init__()
        self.especial = es_especial
        
    @staticmethod
    def crear_nodo(dato: int, es_especial: bool = False, si: "Optional[ArbEsp]" = None, sd: "Optional[ArbEsp]" = None) -> "ArbEsp":
        t = ArbEsp(es_especial)
        t.raiz = NodoAB(dato, si if si is not None else ArbEsp(False), sd if sd is not None else ArbEsp(False))
        return t
        
    def raiz_repetida(self, arbol: "ArbEsp") -> bool:
        return arbol.existe(self.dato())
        
    def insertar_si(self, si: "ArbEsp"):
        if self.raiz_repetida(si):
            raise ValueError('No se puede insertar un subarbol que contenga el valor de la raiz.')
        super().insertar_si(si)

    def insertar_sd(self, sd: "ArbEsp"):
        if self.raiz_repetida(sd):
            raise ValueError('No se puede insertar un subarbol que contenga el valor de la raiz.')
        super().insertar_sd(sd)
        
    def es_nodo_especial(self) -> bool:
        assert self.raiz is not None
        return self.especial
    
    def preorder_especial(self) -> list[int]:
        if self.es_vacio():
            return []
        if self.es_nodo_especial():
            return [self.dato()]
        else:
            return [self.dato()] + self.si().preorder_especial() + self.sd().preorder_especial()
        
    def es_especial(self, val: int) -> bool:
        if self.es_vacio():
            return False
        if self.dato() == val:
            return self.es_nodo_especial()
        else:
            return self.si().es_especial(val) or self.sd().es_especial(val)
         
    def podados(self) -> int:
        def podados_interna(t: ArbEsp, debajo_especial: bool) -> int:
            if t.es_vacio():
                return 0
            if t.es_hoja():
                return 1 if debajo_especial else 0
            else:
                actual = (1 if debajo_especial else 0)
                si = podados_interna(t.si(), debajo_especial or t.es_nodo_especial())
                sd = podados_interna(t.sd(), debajo_especial or t.es_nodo_especial())
                return actual + si + sd
            
        return podados_interna(self, False)
         
    def __str__(self):
        def mostrar(t: ArbEsp, nivel: int):
            tab = '.' * 4
            indent = tab * nivel
            if t.es_vacio():
                return indent + 'AV\n'
            else:
                dato_str = str(t.dato())
                if t.es_nodo_especial():
                    dato_str = f'({dato_str})'
                out = indent + dato_str + '\n'
                out += mostrar(t.si(), nivel + 1)
                out += mostrar(t.sd(), nivel + 1)
                return out
            
        return mostrar(self, 0)

def main():
    t = ArbEsp.crear_nodo(3)
    n2 = ArbEsp.crear_nodo(2, True)
    n1 = ArbEsp.crear_nodo(1)
    n5 = ArbEsp.crear_nodo(5)
    n6 = ArbEsp.crear_nodo(6)
    n7 = ArbEsp.crear_nodo(7, True)
    n0 = ArbEsp.crear_nodo(0)
    n10 = ArbEsp.crear_nodo(10)
    n2.insertar_si(n1)
    n1.insertar_sd(n10)
    n2.insertar_sd(n5)
    n7.insertar_si(n0)
    n6.insertar_sd(n7)
    t.insertar_si(n2)
    t.insertar_sd(n6)
    
    
    print(t)
    print(t.preorder())
    print(t.preorder_especial())
    print(t.es_especial(0))
    print(t.es_especial(2))
    print(t.podados())

if __name__ == '__main__':
    main()
    