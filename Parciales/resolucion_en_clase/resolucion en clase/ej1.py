from collections.abc import Callable
from typing import Any, Generic, Optional, TypeVar
from functools import wraps


class NodoAB:
    def __init__(self, dato: int, si: "Optional[ArbEsp]" = None, sd: "Optional[ArbEsp]" = None, especial: bool = False):
        self.dato: int = dato
        self.si: ArbEsp = ArbEsp() if si is None else si
        self.sd: ArbEsp = ArbEsp() if sd is None else sd
        self.especial: bool = especial

    def __str__(self):
        return self.dato

class ArbEsp:
    def __init__(self):
        self.raiz: Optional[NodoAB] = None

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
    def crear_nodo(
        dato: int, 
        si: "Optional[ArbEsp]" = None, 
        sd: "Optional[ArbEsp]" = None,
        especial: bool = False
    ) -> "ArbEsp":
        t = ArbEsp()
        t.raiz = NodoAB(dato, si, sd, especial)
        return t

    def es_vacio(self) -> bool:
        return self.raiz is None

    @_Decoradores.valida_es_vacio
    def si(self) -> "ArbEsp":
        assert self.raiz is not None
        return self.raiz.si

    @_Decoradores.valida_es_vacio
    def sd(self) -> "ArbEsp":
        assert self.raiz is not None
        return self.raiz.sd

    def es_hoja(self) -> bool:
        return not self.es_vacio() and self.si().es_vacio() and self.sd().es_vacio()

    @_Decoradores.valida_es_vacio
    def dato(self) -> int:
        assert self.raiz is not None
        return self.raiz.dato

    @_Decoradores.valida_es_vacio
    def insertar_si(self, si: "ArbEsp"):
        assert self.raiz is not None
        self.raiz.si = si

    @_Decoradores.valida_es_vacio
    def insertar_sd(self, sd: "ArbEsp"):
        assert self.raiz is not None
        self.raiz.sd = sd

    def set_raiz(self, nodo: NodoAB):
        self.raiz = nodo

    def altura(self) -> int:
        if self.es_vacio():
            return 0
        else:
            return 1 + max(self.si().altura(), self.sd().altura())

    def __len__(self) -> int:
        if self.es_vacio():
            return 0
        else:
            return 1 + len(self.si()) + len(self.sd())

    def __str__(self):
        def mostrar(t: ArbEsp, nivel: int):
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

    def inorder(self) -> list[int]:
        if self.es_vacio():
            return []
        else:
            return self.si().inorder() + [self.dato()] + self.sd().inorder()

    def preorder(self) -> list[int]:
        if self.es_vacio():
            return []
        else:
            resultado_si = self.si().preorder()
            resultado_sd = self.sd().preorder()
            return [self.dato()] + resultado_si + resultado_sd

    def es_nodo_especial(self) -> bool:
        return not self.es_vacio() and self.raiz.especial   # type: ignore
      
    def preorder_especial(self) -> list[int]:
        if self.es_vacio():
            return []
        elif self.es_nodo_especial():
            return [self.dato()]
        else:
            resultado_si = self.si().preorder_especial()
            resultado_sd = self.sd().preorder_especial()
            return [self.dato()] + resultado_si + resultado_sd
        
    
    def es_especial(self, buscado: int) -> bool:
        if self.es_vacio():
            return False
        elif self.dato() == buscado:
            return self.es_nodo_especial()
        else:
            return self.si().es_especial(buscado) or self.sd().es_especial(buscado)


    def podados(self) -> int:
        if self.es_vacio():
            return 0
        elif self.es_nodo_especial():
            return len(self) - 1
        else:
            return self.si().podados() + self.sd().podados()


if __name__ == '__main__':
    t = ArbEsp.crear_nodo(3, especial=True)
    n2 = ArbEsp.crear_nodo(2, especial=True)
    n1 = ArbEsp.crear_nodo(1)
    n5 = ArbEsp.crear_nodo(5)
    n6 = ArbEsp.crear_nodo(6)
    n7 = ArbEsp.crear_nodo(7, especial=True)
    n0 = ArbEsp.crear_nodo(0)
    n2.insertar_si(n1)
    n2.insertar_sd(n5)
    n7.insertar_si(n0)
    n6.insertar_sd(n7)
    t.insertar_si(n2)
    t.insertar_sd(n6)
    
    print(t.preorder())
    print(t.preorder_especial())
    print(t.es_especial(0))
    print(t.es_especial(2))
    print(t.podados())
