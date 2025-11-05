from typing import Generic, TypeVar, Optional, TypeAlias
from copy import copy

# tipos y clases

T = TypeVar('T')
ListaGenerica: TypeAlias = "Lista[T]"

class Nodo(Generic[T]):
    def __init__(self, dato: T, sig: Optional[ListaGenerica] = None):
        self.dato = dato
        if sig is None:
            self.sig= Lista()
        else:
            self.sig = sig

class Lista(Generic[T]):
    def __init__(self):
        self._head: Optional[Nodo[T]] = None

    # Constructores

    def insertar(self, dato: T):
        actual = copy(self)
        self._head = Nodo(dato, actual)
    
    def agregar_al_final(self, dato: T):
        """Agrega un elemento al final de la lista"""
        if self.es_vacia():
            self.insertar(dato)
        else:
            self._head.sig.agregar_al_final(dato)

    # Proyectoras

    def es_vacia(self) -> bool:
        return self._head is None

    def head(self) -> T:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            return self._head.dato
        
    def tail(self) -> ListaGenerica:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            return self._head.sig.copy()
        
    def ultimo(self) -> T:
        """Devuelve el último elemento de la lista"""
        if self.es_vacia():
            raise IndexError('lista vacia')
        elif self._head.sig.es_vacia():
            return self._head.dato
        else:
            return self._head.sig.ultimo()
    
    def elemento_en(self, pos: int) -> T:
        """Devuelve el elemento en la posición indicada (comienza en 0)"""
        if self.es_vacia():
            raise IndexError('lista vacia o posicion invalida')
        if pos == 0:
            return self.head()
        else:
            return self.tail().elemento_en(pos - 1)
    
    # Copia profunda

    def copy(self) -> ListaGenerica:
        if self.es_vacia():
            return Lista()
        else:
            parcial = self._head.sig.copy()
            actual = Lista()
            actual._head = Nodo(copy(self._head.dato), parcial)
            return actual

    # Operaciones

    def __len__(self):
        if self.es_vacia():
            return 0
        else:
            return 1 + self.tail().__len__()
    
    def contiene(self, elemento: T) -> bool:

        if self.es_vacia():
            return False
        elif self.head() == elemento:
            return True
        else:
            return self.tail().contiene(elemento)
    
    def contar(self, elemento: T) -> int:
        if self.es_vacia():
            return 0
        else:
            cuenta = 1 if self.head() == elemento else 0
            return cuenta + self.tail().contar(elemento)
    
    def posicion(self, elemento: T) -> int:
        """Devuelve la posición de la primera ocurrencia del elemento (o -1 si no está)"""
        def _posicion_aux(lista: Lista[T], elemento: T, pos: int) -> int:
            if lista.es_vacia():
                return -1
            elif lista.head() == elemento:
                return pos
            else:
                return _posicion_aux(lista.tail(), elemento, pos + 1)
        
        return _posicion_aux(self, elemento, 0)
    
    def invertir(self) -> ListaGenerica:
        """Devuelve una nueva lista con los elementos en orden inverso"""
        def _invertir_aux(lista: Lista[T], acum: Lista[T]) -> Lista[T]:
            if lista.es_vacia():
                return acum
            else:
                acum.insertar(lista.head())
                return _invertir_aux(lista.tail(), acum)
        
        return _invertir_aux(self, Lista())
    
    def concatenar(self, otra: ListaGenerica) -> ListaGenerica:
        """Concatena esta lista con otra"""
        if self.es_vacia():
            return otra.copy()
        else:
            resto = self.tail().concatenar(otra)
            resto.insertar(self.head())
            return resto
    
    def tomar(self, n: int) -> ListaGenerica:
        """Devuelve los primeros n elementos"""
        if n <= 0 or self.es_vacia():
            return Lista()
        else:
            resto = self.tail().tomar(n - 1)
            resto.insertar(self.head())
            return resto
    
    def saltar(self, n: int) -> ListaGenerica:
        """Salta los primeros n elementos"""
        if n <= 0 or self.es_vacia():
            return self.copy()
        else:
            return self.tail().saltar(n - 1)
        
    # modificadoras

    def eliminar_primero(self):
        """Elimina el primer elemento de la lista"""
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            self._head = self._head.sig._head
    
    def eliminar_ultimo(self):
        """Elimina el último elemento de la lista"""
        if self.es_vacia():
            raise IndexError('lista vacia')
        elif self._head.sig.es_vacia():
            self._head = None
        else:
            self._head.sig.eliminar_ultimo()
    
    def eliminar_en(self, pos: int):
        """Elimina el elemento en la posición indicada"""
        if self.es_vacia():
            raise IndexError('lista vacia o posicion invalida')
        if pos == 0:
            self.eliminar_primero()
        else:
            self._head.sig.eliminar_en(pos - 1)
    
    def eliminar_valor(self, elemento: T):
        """Elimina la primera ocurrencia del elemento"""
        if self.es_vacia():
            return  # No hace nada si no encuentra el elemento
        elif self.head() == elemento:
            self.eliminar_primero()
        else:
            self._head.sig.eliminar_valor(elemento)
        
    # operadores funcionales

    def map(self, func):
        """Aplica una función a cada elemento y devuelve una nueva lista"""
        if self.es_vacia():
            return Lista()
        else:
            nueva = self.tail().map(func)
            nueva.insertar(func(self.head()))
            return nueva
    
    def filter(self, predicado):
        """Filtra elementos que cumplan el predicado"""
        if self.es_vacia():
            return Lista()
        else:
            resto = self.tail().filter(predicado)
            if predicado(self.head()):
                resto.insertar(self.head())
            return resto
    
    def reduce(self, func, inicial):
        """Reduce la lista a un valor usando una función acumuladora"""
        if self.es_vacia():
            return inicial
        else:
            return self.tail().reduce(func, func(inicial, self.head()))
    
    # reescritura de operadores

    def __str__(self):
        """Representación en string de la lista"""
        if self.es_vacia():
            return "[]"
        
        elementos = []
        actual = self
        while not actual.es_vacia():
            elementos.append(str(actual.head()))
            actual = actual._head.sig
        
        return "[" + ", ".join(elementos) + "]"
    
    def __repr__(self):
        return self.__str__()
    
    def __iter__(self):
        """Permite iterar sobre la lista con for"""
        actual = self
        while not actual.es_vacia():
            yield actual.head()
            actual = actual._head.sig
    
    def __getitem__(self, pos: int) -> T:
        """Permite acceder con notación xs[i]"""
        return self.elemento_en(pos)
    
    def __contains__(self, elemento: T) -> bool:
        """Permite usar 'in': elemento in lista"""
        return self.contiene(elemento)



# Ejemplos de uso

if __name__ == "__main__":
    print("=== TAD Lista - Ejemplos ===\n")
    
    # Crear lista
    xs: Lista[int] = Lista()
    print(f"Lista vacía: {xs}")
    print(f"¿Es vacía? {xs.es_vacia()}\n")
    
    # Insertar elementos
    xs.insertar(4)
    xs.insertar(10)
    xs.insertar(20)
    print(f"Después de insertar 4, 10, 20: {xs}")
    print(f"Longitud: {len(xs)}\n")
    
    # Head y tail
    print(f"head(): {xs.head()}")
    print(f"tail(): {xs.tail()}")
    print(f"último(): {xs.ultimo()}\n")
    
    # Acceso por posición
    print(f"Elemento en posición 0: {xs[0]}")
    print(f"Elemento en posición 1: {xs[1]}")
    print(f"Elemento en posición 2: {xs[2]}\n")
    
    # Búsqueda
    print(f"¿Contiene 10? {xs.contiene(10)}")
    print(f"¿Contiene 99? {xs.contiene(99)}")
    print(f"Posición de 10: {xs.posicion(10)}")
    print(f"Veces que aparece 10: {xs.contar(10)}\n")
    
    # Agregar al final
    xs.agregar_al_final(99)
    print(f"Después de agregar 99 al final: {xs}\n")
    
    # Map, filter, reduce
    ys = xs.map(lambda x: x * 2)
    print(f"Map (x * 2): {ys}")
    
    zs = xs.filter(lambda x: x > 10)
    print(f"Filter (x > 10): {zs}")
    
    suma = xs.reduce(lambda acc, x: acc + x, 0)
    print(f"Reduce (suma): {suma}\n")