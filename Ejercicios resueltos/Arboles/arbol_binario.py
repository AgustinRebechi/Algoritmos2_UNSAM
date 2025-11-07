from typing import Any, Generic, List, Optional, TypeVar

T = TypeVar('T')

class ArbolBinario(Generic[T]):
    def __init__(self):
        self.raiz: Optional[NodoAB[T]] = None
        self.sig_inorder: Optional[NodoAB[T]] = None
        self.altura: int = 0

    def es_vacio(self) -> bool:
        return self.raiz is None
    
    # Operaciones basicas

    def si(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            raise TypeError('Arbol Vacio') 
        return self.raiz.si

    def sd(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            raise TypeError('Arbol Vacio') 
        return self.raiz.sd

    def dato(self) -> T:
        if self.es_vacio():
            raise TypeError('Arbol Vacio') 
        return self.raiz.dato

    def es_hoja(self) -> bool:
        return not self.es_vacio() and self.si().es_vacio() and self.sd().es_vacio()
    
    # Proyectoras

    def insertar_si(self, si: "ArbolBinario[T]"):
        if self.es_vacio():
            raise TypeError('Arbol Vacio') 
        self.raiz.si = si

    def insertar_sd(self, sd: "ArbolBinario[T]"):
        if self.es_vacio():
            raise TypeError('Arbol Vacio') 
        self.raiz.sd = sd

    # Modificadoras

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
    
    # Ejercicio 1 Buscar altura

    def nivel_nodo(self, dato: T) -> int:
        return self.rec_nivel_nodo(dato, 1)

    def rec_nivel_nodo(self, dato: T, actual: int) -> int:

        # Caso base

        if self.es_vacio():
            return 0
        
        # Caso Base 2:

        if self.raiz.dato == dato:
            return actual
        
        ## Recursion: Busco subarboles (sy y sd)

        # 1. Busco subarbol SI

        nivel_si = self.si().rec_nivel_nodo(dato, actual + 1)

        # si nivel_si > 0, se encontro nodo en el si o ramas

        if nivel_si > 0:
            return nivel_si
        
        # 2. Si no encontre en subarbol SI, busco subarbol SD
        
        return self.sd().rec_nivel_nodo(dato, actual + 1)
    
    ## Ejercicio 2: Equals

    def __eq__(self, otro: Any) -> bool:
        
        # 1. Chequeo de Tipos: Si 'otro' no es una instancia de ArbolBinario, no pueden ser iguales.
        if not isinstance(otro, ArbolBinario):
            return NotImplemented  # Permite que Python intente la comparación inversa
        
        # 2. Caso Base 1: Ambos son vacíos.
        if self.es_vacio() and otro.es_vacio():
            return True
            
        # 3. Caso Base 2: Uno es vacío y el otro no (¡no son iguales!).
        if self.es_vacio() or otro.es_vacio():
            return False
            
        # 4. Caso Recursivo: Ambos tienen raíz.
        # Se requiere la "recursión triple": dato, subárbol izquierdo, subárbol derecho.
        
        son_iguales = (
            # a) Los datos de la raíz deben ser iguales
            self.dato() == otro.dato() and 
            
            # b) Los subárboles izquierdos deben ser iguales (recursión)
            self.si() == otro.si() and 
            
            # c) Los subárboles derechos deben ser iguales (recursión)
            self.sd() == otro.sd()
        )
        
        return son_iguales

        ## Ejercicio 3: Recorrido guiado

    def recorrido_guiado(self, camino: List[str]) -> Optional[T]:

        
        # Caso Base 1: El camino está vacío
        if not camino:
            # Si la lista de instrucciones se agotó, hemos llegado al nodo final.
            # Retornamos su dato, pero solo si el árbol actual no es vacío.
            if self.es_vacio():
                return None # No se puede devolver el dato de un árbol vacío
            try:
                return self.dato() 
            except TypeError:
                # Captura el TypeError de dato() si el árbol está vacío
                return None
        
        # Caso Base 2: El árbol es vacío antes de que el camino termine
        if self.es_vacio():
            return None # El camino es inválido
            
        # Caso Recursivo
        
        instruccion = camino[0] # Tomar la primera instrucción
        resto_camino = camino[1:] # El resto de la lista
        
        try:
            if instruccion == 'izquierda':
                # Llamada recursiva sobre el subárbol izquierdo (SI)
                return self.si().recorrido_guiado(resto_camino)
            
            elif instruccion == 'derecha':
                # Llamada recursiva sobre el subárbol derecho (SD)
                return self.sd().recorrido_guiado(resto_camino)
            
            else:
                # Instrucción inválida
                return None

        except TypeError:
            # Captura TypeError si se intenta llamar si() o sd() sobre un árbol vacío
            return None

    ## Ejercicio 3: visita DFS inorder, preorder, postorder y BFS

    def preorder(self) -> List[T]:
        """
        Recorrido PREORDER: Raíz → Izquierda → Derecha
        
        Visito PRIMERO, luego exploro subárboles.
        """
        if self.es_vacio():
            return []
        else:
            # 1. Visito la raíz (la agrego a la lista)
            resultado = [self.dato()]
            
            # 2. Recorro subárbol izquierdo
            resultado.extend(self.si().preorder())
            
            # 3. Recorro subárbol derecho
            resultado.extend(self.sd().preorder())
            
            return resultado
    
    def inorder(self) -> List[T]:
        """
        Recorrido INORDER: Izquierda → Raíz → Derecha
        
        Visito EN EL MEDIO de explorar subárboles.
        ¡Solo funciona para árboles binarios!
        """
        if self.es_vacio():
            return []
        else:
            resultado = []
            
            # 1. Recorro subárbol izquierdo
            resultado.extend(self.si().inorder())
            
            # 2. Visito la raíz
            resultado.append(self.dato())
            
            # 3. Recorro subárbol derecho
            resultado.extend(self.sd().inorder())
            
            return resultado
    
    def postorder(self) -> List[T]:
        """
        Recorrido POSTORDER: Izquierda → Derecha → Raíz
        
        Visito AL FINAL, después de explorar subárboles.
        """
        if self.es_vacio():
            return []
        else:
            resultado = []
            
            # 1. Recorro subárbol izquierdo
            resultado.extend(self.si().postorder())
            
            # 2. Recorro subárbol derecho
            resultado.extend(self.sd().postorder())
            
            # 3. Visito la raíz
            resultado.append(self.dato())
            
            return resultado
    
    # ============================================
    # RECORRIDO BFS QUE DEVUELVE LISTA
    # ============================================
    
    def bfs(self) -> List[T]:
        """
        Recorrido BFS (Breadth-First Search): Por niveles
        
        Usa una cola explícita para recorrer nivel por nivel.
        """
        if self.es_vacio():
            return []
        
        resultado = []
        cola: List[ArbolBinario[T]] = [self]  # Empiezo con la raíz
        
        while cola:
            # Desencolo el primer árbol
            actual = cola.pop(0)
            
            if not actual.es_vacio():
                # Visito el nodo actual
                resultado.append(actual.dato())
                
                # Encolo sus hijos (izquierdo y derecho)
                cola.append(actual.si())
                cola.append(actual.sd())
        
        return resultado

    def __repr__(self) -> str:
        """Representación visual del árbol"""
        if self.es_vacio():
            return "Ø"
        if self.es_hoja():
            return f"[{self.dato()}]"
        return f"({self.dato()}: {self.si().__repr__()} | {self.sd().__repr__()})"        
    
    # Ejercicio 4: Bottom-up

    def bottom_up(self) -> List[T]:
        """
        Recorrido desde las hojas hasta la raíz, de izquierda a derecha.
        
        Estrategia 1: BFS invertido
        - Hacer BFS normal
        - Invertir el resultado
        
        Ejemplo:
                 4
               /   \\
              2     5
             / \\     \\
            1   3     7
                     / \\
                    6   8
        
        BFS normal:  [4, 2, 5, 1, 3, 7, 6, 8]
        Bottom-up:   [1, 3, 6, 8, 2, 7, 5, 4]
        """
        if self.es_vacio():
            return []
        
        # Usar BFS pero guardar en orden inverso
        resultado = []
        cola = [self]
        
        while cola:
            actual = cola.pop(0)
            
            if not actual.es_vacio():
                # Insertar al INICIO en vez de al final
                resultado.insert(0, actual.dato())
                
                # Importante: encolar primero derecho, luego izquierdo
                # para que al invertir queden en el orden correcto
                cola.append(actual.si())
                cola.append(actual.sd())
        
        return resultado
    
    # Ejercicio 5: Eliminar recursion en DFS inorder (usar recursion de cola)

    def inorder_iterativo(self) -> List[T]:
        """
        Inorder iterativo usando pila explícita.
        
        Estrategia:
        1. Ir lo más a la izquierda posible, apilando nodos
        2. Cuando no puedo ir más a la izquierda:
           a. Desapilar y visitar
           b. Ir a la derecha
        3. Repetir
        
        Simula exactamente lo que hace la recursión:
        - La pila reemplaza la pila de recursión
        - "Ir a la izquierda" = antes de visitar
        - "Visitar" = cuando vuelvo de la izquierda
        - "Ir a la derecha" = después de visitar
        """
        if self.es_vacio():
            return []
        
        resultado = []
        pila: List[ArbolBinario[T]] = []
        actual = self
        
        while True:
            # FASE 1: Ir lo más a la izquierda posible
            while not actual.es_vacio():
                pila.append(actual)
                actual = actual.si()
            
            # FASE 2: Si la pila está vacía, terminamos
            if not pila:
                break
            
            # FASE 3: Desapilar y visitar
            actual = pila.pop()
            resultado.append(actual.dato())
            
            # FASE 4: Ir a la derecha
            actual = actual.sd()
        
        return resultado


    
class NodoAB(Generic[T]):

    def __init__(
        self, 
        dato: T, 
        si: Optional[ArbolBinario[T]] = None, 
        sd: Optional[ArbolBinario[T]] = None
    ):
        self.dato: T = dato
        self.si: ArbolBinario[T] = ArbolBinario() if si is None else si
        self.sd: ArbolBinario[T] = ArbolBinario() if sd is None else sd

    @staticmethod
    def crear_nodo(
        dato: T, 
        si: Optional[ArbolBinario[T]] = None, 
        sd: Optional[ArbolBinario[T]] = None
    ) -> ArbolBinario[T]:
        
        t = ArbolBinario()
        t.raiz = NodoAB(dato, si, sd)
        return t
    

if __name__ == "__main__":
    print("=" * 60)
    print("RECORRIDOS DE ÁRBOL BINARIO")
    print("=" * 60)
    print()
    
    # Construir el árbol del documento:
    #         4
    #       /   \
    #      2     5
    #     / \     \
    #    1   3     7
    #             / \
    #            6   8
    
    # Nivel 3 (hojas)
    A1 = NodoAB.crear_nodo(1)
    A3 = NodoAB.crear_nodo(3)
    A6 = NodoAB.crear_nodo(6)
    A8 = NodoAB.crear_nodo(8)
    
    # Nivel 2
    A2 = NodoAB.crear_nodo(2, si=A1, sd=A3)
    A7 = NodoAB.crear_nodo(7, si=A6, sd=A8)
    
    # Nivel 1 (raíz)
    A5 = NodoAB.crear_nodo(5, sd=A7)
    arbol = NodoAB.crear_nodo(4, si=A2, sd=A5)

    camino1 = ['izquierda', 'derecha']  # Debería llevar al nodo con dato '7'
    resultado1 = A1.recorrido_guiado(camino1)
    print(f"Resultado del recorrido guiado {camino1}: {resultado1}")  # Esperado: 7 

    print("--- Niveles encontrados ---")
    print(f"Nivel de '1' (Raíz): {A1.nivel_nodo(1)}")
    print(f"Nivel de '6' : {A1.nivel_nodo(6)}")
    print(f"Nivel de '7' : {A1.nivel_nodo(7)}")
    print(f"Nivel de '5' : {A1.nivel_nodo(5)}")
    print(f"Nivel de '8' : {A1.nivel_nodo(8)}")
    print(f"Nivel de '99' (No existe): {A1.nivel_nodo(99)}")

    print("=" * 60)
    print("RECORRIDOS DFS")
    print("=" * 60)
    print()

    preorder_result = arbol.preorder()
    print(f"PREORDER (Raíz → Izq → Der):")
    print(f"  Resultado: {preorder_result}")
    print(f"  Esperado:  [4, 2, 1, 3, 5, 7, 6, 8]")
    print(f"  ✓ Correcto" if preorder_result == [4, 2, 1, 3, 5, 7, 6, 8] else "  ✗ Error")
    print()
    
    inorder_result = arbol.inorder()
    print(f"INORDER (Izq → Raíz → Der):")
    print(f"  Resultado: {inorder_result}")
    print(f"  Esperado:  [1, 2, 3, 4, 5, 6, 7, 8]")
    print(f"  ✓ Correcto" if inorder_result == [1, 2, 3, 4, 5, 6, 7, 8] else "  ✗ Error")
    print()
    
    postorder_result = arbol.postorder()
    print(f"POSTORDER (Izq → Der → Raíz):")
    print(f"  Resultado: {postorder_result}")
    print(f"  Esperado:  [1, 3, 2, 6, 8, 7, 5, 4]")
    print(f"  ✓ Correcto" if postorder_result == [1, 3, 2, 6, 8, 7, 5, 4] else "  ✗ Error")
    print()

    print("=" * 60)
    print("RECORRIDO BFS")
    print("=" * 60)
    print()
    
    bfs_result = arbol.bfs()
    print(f"BFS (Por niveles):")
    print(f"  Resultado: {bfs_result}")
    print(f"  Esperado:  [4, 2, 5, 1, 3, 7, 6, 8]")
    print(f"  ✓ Correcto" if bfs_result == [4, 2, 5, 1, 3, 7, 6, 8] else "  ✗ Error")
    print()
    
    print("Explicación BFS:")
    print("  Nivel 0: [4]")
    print("  Nivel 1: [2, 5]")
    print("  Nivel 2: [1, 3, 7]")
    print("  Nivel 3: [6, 8]")
    print()
