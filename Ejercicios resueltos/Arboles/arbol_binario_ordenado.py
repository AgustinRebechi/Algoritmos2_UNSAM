from typing import TypeVar, Optional, Protocol
from arbol_binario import NodoAB, ArbolBinario
T = TypeVar("T")

# Un "Protocol" es una forma especial de indicar qué métodos o funciones debe tener una clase.
# Es como una lista de reglas que una clase tiene que seguir si quiere ser considerada "Comparable".
# En este caso, decimos que cualquier cosa "Comparable" debe poder compararse con <, <=, >, >=, == y !=
# Notá que usamos "..." en vez de código dentro de cada función. Esto se llama "elipsis".
# Es un marcador que indica que la función está definida solo como estructura, pero no tiene código real.
# En este contexto, los "..." funcionan igual que "pass", pero se usan más comúnmente cuando definimos tipos o estructuras abstractas.
# Diferencia entre "..." y "pass":
# - "..." es elipsis, se usa cuando querés decir "esto se define más adelante o en otro lugar"
# - "pass" significa "no hacer nada", y se usa para evitar errores en funciones vacías


class Comparable(Protocol):  # Creamos un protocolo (como una interfaz en otros lenguajes)
    def __lt__(self: 'T', otro: 'T') -> bool: ...
    def __le__(self: 'T', otro: 'T') -> bool: ...
    def __gt__(self: 'T', otro: 'T') -> bool: ...
    def __ge__(self: 'T', otro: 'T') -> bool: ...
    def __eq__(self: 'T', otro: 'T') -> bool: ...
    def __ne__(self: 'T', otro: 'T') -> bool: ...


# Definimos la clase NodoABO, que hereda de NodoAB y trabaja con elementos de tipo T
class NodoABO(NodoAB[T]):
    # Constructor que inicializa el nodo con un valor y dos árboles vacíos como hijos
    def __init__(self, dato: T):
        # Llama al constructor de la superclase NodoAB
        super().__init__(dato, ArbolBinarioOrdenado(), ArbolBinarioOrdenado())

    # Define el operador menor que entre nodos
    def __lt__(self, otro: "NodoABO[T]") -> bool:
        # Compara los datos de los nodos si 'otro' es también un NodoABO
        return isinstance(otro, NodoABO) and self.dato < otro.dato

    # Define el operador mayor que entre nodos
    def __gt__(self, otro: "NodoABO[T]") -> bool:
        # Compara los datos de los nodos si 'otro' es también un NodoABO
        return isinstance(otro, NodoABO) and self.dato > otro.dato

    # Define el operador de igualdad entre nodos
    def __eq__(self, otro: "NodoABO[T]") -> bool:
        # Verifica si los datos de ambos nodos son iguales
        return isinstance(otro, NodoABO) and self.dato == otro.dato

class ArbolBinarioOrdenado(ArbolBinario[T]):
        # Método estático que crea un nuevo nodo con el valor 'dato' y lo coloca como raíz de un nuevo árbol binario
    @staticmethod
    def crear_nodo(dato: T) -> "ArbolBinarioOrdenado[T]":
        # Crea una nueva instancia de ArbolBinarioOrdenado
        nuevo = ArbolBinarioOrdenado()
        # Asigna el nodo con 'dato' como la raíz del nuevo árbol
        nuevo.set_raiz(NodoABO(dato))
        # Devuelve el nuevo árbol
        return nuevo

    # Método que verifica si el árbol binario está ordenado
    def es_ordenado(self) -> bool:
        # Función interna recursiva que comprueba si el subárbol está ordenado
        # en base a sus valores mínimos y máximos permitidos
        #minimo: Indica el valor mínimo permitido para los nodos del subárbol actual. Es decir, todos los nodos en el subárbol izquierdo deben ser mayores que este valor mínimo.
        #maximo: Indica el valor máximo permitido para los nodos del subárbol actual. Esto significa que todos los nodos en el subárbol
        #derecho deben ser menores que este valor máximo.
        def es_ordenado_interna(arbol: "ArbolBinarioOrdenado[T]",   minimo: Optional[T] = None, maximo: Optional[T] = None ) -> bool:
            # Si el árbol está vacío, se considera ordenado
            if arbol.es_vacio():
                return True
            # Verifica si el valor del nodo actual está fuera de los límites mínimo o máximo
            if (minimo is not None and arbol.dato() <= minimo) or (maximo is not None and arbol.dato() >= maximo):
                return False
            # Verifica recursivamente los subárboles izquierdo y derecho
            return es_ordenado_interna(arbol.si(), minimo, arbol.dato()) and es_ordenado_interna(arbol.sd(), arbol.dato(), maximo)

        # Inicia la verificación desde la raíz del árbol
        return es_ordenado_interna(self)

    # Inserta un subárbol en el hijo izquierdo del árbol actual y comprueba si sigue siendo ordenado
    def insertar_si(self, arbol: "ArbolBinarioOrdenado[T]"):
        si = self.si()  # Almacena temporalmente el subárbol izquierdo actual
        super().insertar_si(arbol)  # Inserta el nuevo subárbol
        if not self.es_ordenado():  # Si el árbol resultante no está ordenado
            super().insertar_si(si)  # Restaura el subárbol anterior
            raise ValueError("El árbol a insertar no es ordenado o viola la propiedad de orden del árbol actual")

    # Inserta un subárbol en el hijo derecho del árbol actual y comprueba si sigue siendo ordenado
    def insertar_sd(self, arbol: "ArbolBinarioOrdenado[T]"):
        sd = self.sd()  # Almacena temporalmente el subárbol derecho actual
        super().insertar_sd(arbol)  # Inserta el nuevo subárbol
        if not self.es_ordenado():  # Si el árbol resultante no está ordenado
            super().insertar_sd(sd)  # Restaura el subárbol anterior
            raise ValueError("El árbol a insertar no es ordenado o viola la propiedad de orden del árbol actual")

    # Inserta un valor en el árbol de manera ordenada
    def insertar(self, valor: T):
          # Primero revisamos si el árbol está vacío (no tiene raíz)
        if self.es_vacio():
            # Si está vacío, creamos un nuevo nodo con el valor y lo ponemos como raíz del árbol
            self.set_raiz(NodoABO(valor))
        # Si el árbol NO está vacío, hay que decidir si el valor va a la izquierda o a la derecha
        elif valor < self.dato():
            # Si el valor que queremos insertar es menor que el dato actual del nodo raíz...
            # ...entonces lo insertamos en el subárbol izquierdo (llamamos recursivamente a insertar sobre el hijo izquierdo)
            self.si().insertar(valor)
        else:
            # Si el valor es mayor o igual que el dato del nodo raíz...
            # ...entonces lo insertamos en el subárbol derecho (llamamos recursivamente a insertar sobre el hijo derecho)
            self.sd().insertar(valor)
        # Nota: Esta forma de insertar mantiene el árbol ordenado.
        # Siempre los menores van a la izquierda y los mayores o iguales a la derecha.


    # Busca un valor en el árbol
    def buscar(self, valor: T) -> bool:
      pass

    # Encuentra el valor máximo en el árbol
    def maximo(self) -> "Optional[T]":
      pass

    # Encuentra el valor mínimo en el árbol
    def minimo(self) -> Optional[T]:
      pass

    def _encontrar_min(self, arbol: "ArbolBinarioOrdenado[T]") -> "ArbolBinarioOrdenado[T]":
      pass

    def _encontrar_max(self, arbol: "ArbolBinarioOrdenado[T]") -> "ArbolBinarioOrdenado[T]":
      pass

    def eliminar_por_copia(self, valor: T) -> None:
       pass

    def eliminar_por_fusion(self, valor: T) -> None:
       pass

def main():

    t: ArbolBinarioOrdenado[int] = ArbolBinarioOrdenado()
    t.insertar(10)
    t.insertar(5)
    t.insertar(15)
    t.insertar(2)
    t.insertar(7)
    t.insertar(12)
    t.insertar(17)
    t.insertar(20)
    t.insertar(13)
    print(t.es_ordenado())
    print(t)
    print("Eliminar por fusion valor existente")
    t.eliminar_por_fusion(20)
    print(t)
    print("Eliminar por fusion valor inexistente")
    t.eliminar_por_fusion(100)
    print(t)
    print("Eliminar por copia valor existente")
    t.eliminar_por_fusion(2)
    print(t)
    print("Eliminar por copia valor inexistente")
    t.eliminar_por_fusion(100)
    print(t)


  #  t2: ArbolBinarioOrdenado[int] = ArbolBinarioOrdenado()
  #  t2.insertar(8)
    # t2.insertar(11)   # Descomentar para probar la excepción al violar el orden
  #  t2.insertar(6)
  #  t.insertar_si(t2)
  #  print(t)
  #  print(f'Ordenado?: {t.es_ordenado()}')
  #  print(f'Tiene 12: {t.buscar(12)}')
  #  print(f'Tiene 0: {t.buscar(0)}')
  #  print(f'Tiene 10: {t.buscar(10)}')
  #  print(f'Tiene 5: {t.buscar(5)}')
  #  print(f'Tiene 6: {t.buscar(6)}')
  #  print("Minimo:",t.minimo())

  #  print(t.valores_menores_a(6))
  #  print(t.recorrer_mayor_a_menor())
if __name__ == "__main__":
    main()