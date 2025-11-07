from functools import reduce
from typing import Any, Generic, TypeVar

T = TypeVar('T')

class ArbolN(Generic[T]):
    def __init__(self, dato: T):
        self._dato: T = dato
        self._subarboles: list['ArbolN[T]'] = []

    # ============================================
    # PROPERTIES
    # ============================================
    
    @property
    def dato(self) -> T:
        return self._dato

    @dato.setter
    def dato(self, valor: T):
        self._dato = valor

    @property
    def subarboles(self) -> list['ArbolN[T]']:
        return self._subarboles

    @subarboles.setter
    def subarboles(self, subarboles: list['ArbolN[T]']):
        self._subarboles = subarboles
    
    # ============================================
    # OPERACIONES BÁSICAS
    # ============================================
    
    def insertar_subarbol(self, subarbol: 'ArbolN[T]'):
        """Agrega un subárbol como hijo"""
        self.subarboles.append(subarbol)

    def es_hoja(self) -> bool:
        """Verifica si el nodo no tiene hijos"""
        return self.subarboles == []
    
    def altura(self) -> int:
        """Calcula la altura del árbol"""
        if self.es_hoja():
            return 1
        else:
            return 1 + max([subarbol.altura() for subarbol in self.subarboles])
    
    def __len__(self) -> int:
        """Calcula la cantidad total de nodos"""
        if self.es_hoja():
            return 1
        else:
            return 1 + sum([len(subarbol) for subarbol in self.subarboles])
    
    # ============================================
    # EJERCICIO: IGUALDAD
    # ============================================
    
    def __eq__(self, otro: Any) -> bool:
        """
        Verifica si dos árboles N-arios son iguales.
        
        Dos árboles son iguales si:
        1. Sus datos son iguales
        2. Tienen la misma cantidad de subárboles
        3. Cada subárbol en la misma posición es igual (recursivamente)
        
        VERSIÓN 1: Con loop explícito (más claro)
        """
        # 1. Verificar tipo
        if not isinstance(otro, ArbolN):
            return False
        
        # 2. Comparar datos
        if self.dato != otro.dato:
            return False
        
        # 3. Comparar cantidad de subárboles
        if len(self.subarboles) != len(otro.subarboles):
            return False
        
        # 4. Comparar cada subárbol recursivamente
        for i in range(len(self.subarboles)):
            if self.subarboles[i] != otro.subarboles[i]:
                return False
        
        # 5. Si llegamos acá, son iguales
        return True
    
    def equals_v2(self, otro: Any) -> bool:
        """
        VERSIÓN 2: Con zip y all (más pythónica)
        """
        if not isinstance(otro, ArbolN):
            return False
        
        # Comparar datos y cantidad
        if self.dato != otro.dato or len(self.subarboles) != len(otro.subarboles):
            return False
        
        # Comparar todos los subárboles recursivamente
        return all(
            sub1.equals_v2(sub2) 
            for sub1, sub2 in zip(self.subarboles, otro.subarboles)
        )
    
    def equals_v3(self, otro: Any) -> bool:
        """
        VERSIÓN 3: Todo en una línea (funcional)
        """
        return (
            isinstance(otro, ArbolN) and
            self.dato == otro.dato and
            len(self.subarboles) == len(otro.subarboles) and
            all(sub1.equals_v3(sub2) for sub1, sub2 in zip(self.subarboles, otro.subarboles))
        )
    
    # ============================================
    # VERSIÓN CON RECURSIÓN MUTUA (la del documento)
    # ============================================
    
    def equals_mutua(self, otro: Any) -> bool:
        """
        VERSIÓN 4: Con recursión mutua
        
        Usa dos funciones:
        - Una compara UN árbol con otro
        - Otra compara UNA LISTA de árboles con otra lista
        """
        def bosques_iguales(
            bosque1: list['ArbolN[T]'], 
            bosque2: list['ArbolN[T]']
        ) -> bool:
            """Compara dos listas de árboles"""
            # Caso base 1: Ambas listas vacías
            if not bosque1 and not bosque2:
                return True
            
            # Caso base 2: Una vacía y otra no
            if not bosque1 or not bosque2:
                return False
            
            # Caso base 3: Diferente cantidad de árboles
            if len(bosque1) != len(bosque2):
                return False
            
            # Caso recursivo: Comparar el primero y luego el resto
            return (
                bosque1[0].equals_mutua(bosque2[0]) and  # Compara primer árbol
                bosques_iguales(bosque1[1:], bosque2[1:])  # Compara resto
            )
        
        # Función principal
        if not isinstance(otro, ArbolN):
            return False
        
        # Comparar dato y luego los bosques
        return (
            self.dato == otro.dato and
            bosques_iguales(self.subarboles, otro.subarboles)
        )
    # ============================================
    # PREORDER (del documento)
    # ============================================
    
    def preorder_funcional(self) -> list[T]:
        """
        PREORDER con reduce (versión funcional del documento)
        
        Lógica:
        1. Empiezo con [mi_dato]
        2. Para cada subárbol, concateno su preorder
        """
        return reduce(
            lambda recorrido, subarbol: recorrido + subarbol.preorder_funcional(), 
            self.subarboles, 
            [self.dato]
        )
    
    def preorder_imperativo(self) -> list[T]:
        """
        PREORDER con loop (versión imperativa del documento)
        
        Lógica:
        1. Visito la raíz (agrego mi dato)
        2. Visito todos mis subárboles de izquierda a derecha
        """
        recorrido = [self.dato]  # Primero YO
        for subarbol in self.subarboles:  # Luego MIS HIJOS
            recorrido += subarbol.preorder_imperativo()
        return recorrido
    
    def preorder_mutua(self) -> list[T]:
        """
        PREORDER con recursión mutua (versión del documento)
        
        Usa dos funciones:
        - preorder: procesa UN árbol
        - preorder_n: procesa UNA LISTA de árboles
        """
        def preorder_n(bosque: list['ArbolN[T]']) -> list[T]:
            """Procesa una lista de árboles"""
            if not bosque:
                return []
            else:
                # Primer árbol + resto recursivamente
                return bosque[0].preorder_mutua() + preorder_n(bosque[1:])

        # Mi dato + mis subárboles
        return [self.dato] + preorder_n(self.subarboles)
    
    # ============================================
    # EJERCICIO 1: POSTORDER
    # ============================================
    
    def postorder_directo(self) -> list[T]:
        """
        POSTORDER con recursión múltiple directa
        
        Lógica:
        1. Visito todos mis subárboles primero
        2. Luego visito la raíz (yo)
        """
        recorrido = []
        
        # Primero MIS HIJOS
        for subarbol in self.subarboles:
            recorrido += subarbol.postorder_directo()
        
        # Luego YO
        recorrido.append(self.dato)
        
        return recorrido
    
    def postorder_funcional(self) -> list[T]:
        """
        POSTORDER con reduce (versión funcional)
        """
        return reduce(
            lambda recorrido, subarbol: recorrido + subarbol.postorder_funcional(),
            self.subarboles,
            []  # Empiezo con lista vacía
        ) + [self.dato]  # Agrego mi dato AL FINAL
    
    def postorder_mutua(self) -> list[T]:
        """
        POSTORDER con recursión mutua
        
        Usa dos funciones:
        - postorder: procesa UN árbol
        - postorder_n: procesa UNA LISTA de árboles
        """
        def postorder_n(bosque: list['ArbolN[T]']) -> list[T]:
            """Procesa una lista de árboles"""
            if not bosque:
                return []
            else:
                # Primer árbol + resto recursivamente
                return bosque[0].postorder_mutua() + postorder_n(bosque[1:])
        
        # Mis subárboles + mi dato (AL REVÉS que preorder)
        return postorder_n(self.subarboles) + [self.dato]
    
    # ============================================
    # BFS (del documento)
    # ============================================
    
    def bfs_original(self) -> list[T]:
        """
        BFS original del documento (usa visitar, no devuelve)
        Adaptado para devolver lista
        """
        resultado = []
        
        def recorrer():
            if q:
                actual = q.pop()                    # desencolar árbol visitado
                resultado.append(actual.dato)       # visitar
                for subarbol in actual.subarboles:  # para cada subárbol
                    q.insert(0, subarbol)           # encolar subárbol
                recorrer()
        
        q: list['ArbolN[T]'] = [self]               # encolar raíz
        recorrer()
        return resultado
    
    # ============================================
    # EJERCICIO 2: BFS que devuelve lista
    # ============================================
    
    def bfs(self) -> list[T]:
        """
        BFS iterativo (más claro)
        
        Usa una COLA (FIFO):
        1. Encolo la raíz
        2. Mientras haya elementos en la cola:
           a. Desencolo
           b. Visito (agrego a resultado)
           c. Encolo todos sus hijos
        """
        if self.es_hoja():
            return [self.dato]
        
        resultado = []
        cola = [self]  # Empiezo con la raíz
        
        while cola:
            actual = cola.pop(0)  # Desencolo (FIFO)
            resultado.append(actual.dato)  # Visito
            
            # Encolo TODOS los hijos
            for subarbol in actual.subarboles:
                cola.append(subarbol)
        
        return resultado
    
    def bfs_recursivo(self) -> list[T]:
        """
        BFS recursivo (versión del documento mejorada)
        """
        def recorrer_cola(cola: list['ArbolN[T]'], acumulado: list[T]) -> list[T]:
            """Recursión de cola con acumulador"""
            if not cola:
                return acumulado
            
            actual = cola.pop(0)  # Desencolo
            acumulado.append(actual.dato)  # Visito
            
            # Encolo todos los hijos
            for subarbol in actual.subarboles:
                cola.append(subarbol)
            
            return recorrer_cola(cola, acumulado)
        
        return recorrer_cola([self], [])

    # ============================================
    # COPY
    # ============================================

    def copy(self) -> 'ArbolN[T]':
        """
        Con list comprehension (más compacta)
        """
        nuevo_arbol = ArbolN(self.dato)
        nuevo_arbol.subarboles = [sub.copy_v2() for sub in self.subarboles]
        return nuevo_arbol



    
    # ============================================
    # UTILIDADES PARA TESTING
    # ============================================
    
    def __repr__(self) -> str:
        """Representación del árbol para debugging"""
        if self.es_hoja():
            return f"[{self.dato}]"
        else:
            hijos_repr = ", ".join([repr(sub) for sub in self.subarboles])
            return f"({self.dato}: {hijos_repr})"
    
    def __str__(self) -> str:
        """Representación legible del árbol"""
        return self._str_helper(0)
    
    def _str_helper(self, nivel: int) -> str:
        """Helper recursivo para imprimir el árbol"""
        indent = "  " * nivel
        resultado = f"{indent}{self.dato}\n"
        for subarbol in self.subarboles:
            resultado += subarbol._str_helper(nivel + 1)
        return resultado


# ============================================
# EJEMPLOS Y PRUEBAS
# ============================================

if __name__ == "__main__":
    print("=" * 70)
    print("ÁRBOL N-ARIO: EJERCICIO DE IGUALDAD")
    print("=" * 70)
    print()
    
    # ============================================
    # EJEMPLO 1: Árboles iguales
    # ============================================
    
    print("EJEMPLO 1: Árboles iguales")
    print("-" * 70)
    
    # Construir árbol 1:
    #       A
    #      /|\
    #     B C D
    #     |
    #     E
    
    arbol1 = ArbolN('A')
    b1 = ArbolN('B')
    c1 = ArbolN('C')
    d1 = ArbolN('D')
    e1 = ArbolN('E')
    
    b1.insertar_subarbol(e1)
    arbol1.insertar_subarbol(b1)
    arbol1.insertar_subarbol(c1)
    arbol1.insertar_subarbol(d1)
    
    # Construir árbol 2 (exactamente igual)
    arbol2 = ArbolN('A')
    b2 = ArbolN('B')
    c2 = ArbolN('C')
    d2 = ArbolN('D')
    e2 = ArbolN('E')
    
    b2.insertar_subarbol(e2)
    arbol2.insertar_subarbol(b2)
    arbol2.insertar_subarbol(c2)
    arbol2.insertar_subarbol(d2)
    
    print("Árbol 1:")
    print(arbol1)
    print("Árbol 2:")
    print(arbol2)
    
    print("Comparaciones:")
    print(f"  __eq__ (v1):       {arbol1 == arbol2}")
    print(f"  equals_v2:         {arbol1.equals_v2(arbol2)}")
    print(f"  equals_v3:         {arbol1.equals_v3(arbol2)}")
    print(f"  equals_mutua:      {arbol1.equals_mutua(arbol2)}")
    print(f"  Esperado: True")
    print()
    
    # ============================================
    # EJEMPLO 2: Datos diferentes
    # ============================================
    
    print("EJEMPLO 2: Datos diferentes")
    print("-" * 70)
    
    arbol3 = ArbolN('X')  # Raíz diferente
    arbol3.insertar_subarbol(ArbolN('B'))
    arbol3.insertar_subarbol(ArbolN('C'))
    
    print("Árbol 1:")
    print(arbol1)
    print("Árbol 3:")
    print(arbol3)
    
    print(f"¿Son iguales? {arbol1 == arbol3}")
    print(f"Esperado: False (datos diferentes)")
    print()
    
    # ============================================
    # EJEMPLO 3: Cantidad de hijos diferente
    # ============================================
    
    print("EJEMPLO 3: Cantidad de hijos diferente")
    print("-" * 70)
    
    arbol4 = ArbolN('A')
    arbol4.insertar_subarbol(ArbolN('B'))
    arbol4.insertar_subarbol(ArbolN('C'))
    # Falta 'D'
    
    print("Árbol 1 (3 hijos):")
    print(arbol1)
    print("Árbol 4 (2 hijos):")
    print(arbol4)
    
    print(f"¿Son iguales? {arbol1 == arbol4}")
    print(f"Esperado: False (diferente cantidad de hijos)")
    print()
    
    # ============================================
    # EJEMPLO 4: Orden diferente
    # ============================================
    
    print("EJEMPLO 4: Orden diferente de hijos")
    print("-" * 70)
    
    arbol5 = ArbolN('A')
    arbol5.insertar_subarbol(ArbolN('D'))  # Orden invertido
    arbol5.insertar_subarbol(ArbolN('C'))
    arbol5.insertar_subarbol(ArbolN('B'))
    
    print("Árbol 1 (B, C, D):")
    print(arbol1)
    print("Árbol 5 (D, C, B):")
    print(arbol5)
    
    print(f"¿Son iguales? {arbol1 == arbol5}")
    print(f"Esperado: False (orden diferente)")
    print()
    
    # ============================================
    # EJEMPLO 5: Hojas iguales
    # ============================================
    
    print("EJEMPLO 5: Hojas iguales")
    print("-" * 70)
    
    hoja1 = ArbolN(42)
    hoja2 = ArbolN(42)
    
    print(f"Hoja 1: {hoja1}")
    print(f"Hoja 2: {hoja2}")
    print(f"¿Son iguales? {hoja1 == hoja2}")
    print(f"Esperado: True")
    print()
    
    # ============================================
    # EJEMPLO 6: Profundidad diferente
    # ============================================
    
    print("EJEMPLO 6: Profundidad diferente")
    print("-" * 70)
    
    # Árbol poco profundo
    arbol6 = ArbolN('A')
    arbol6.insertar_subarbol(ArbolN('B'))
    
    # Árbol más profundo
    arbol7 = ArbolN('A')
    b_prof = ArbolN('B')
    b_prof.insertar_subarbol(ArbolN('C'))
    arbol7.insertar_subarbol(b_prof)
    
    print("Árbol 6 (altura 2):")
    print(arbol6)
    print("Árbol 7 (altura 3):")
    print(arbol7)
    
    print(f"¿Son iguales? {arbol6 == arbol7}")
    print(f"Esperado: False (estructura diferente)")
    print()
    # ============================================
    # PREORDER
    # ============================================
    
    print("=" * 70)
    print("PREORDER (Raíz → Hijos)")
    print("=" * 70)
    print()
    
    pre_func = arbol1.preorder_funcional()
    pre_imp = arbol1.preorder_imperativo()
    pre_mut = arbol1.preorder_mutua()
    
    print("Versiones de PREORDER:")
    print(f"  Funcional (reduce):  {pre_func}")
    print(f"  Imperativo (loop):   {pre_imp}")
    print(f"  Mutua (recursión):   {pre_mut}")
    print()
    
    print("Verificación:")
    todas_iguales = pre_func == pre_imp == pre_mut
    print(f"  {'✓ Todas iguales' if todas_iguales else '✗ Diferentes'}")
    print(f"  Esperado: ['A', 'B', 'E', 'C', 'D']")
    print()
    
    print("Explicación del orden:")
    print("  1. Visito A (raíz)")
    print("  2. Visito subárbol B:")
    print("     2.1. Visito B")
    print("     2.2. Visito subárbol E:")
    print("          2.2.1. Visito E (hoja)")
    print("  3. Visito subárbol C:")
    print("     3.1. Visito C (hoja)")
    print("  4. Visito subárbol D:")
    print("     4.1. Visito D (hoja)")
    print()
    
    # ============================================
    # EJERCICIO 1: POSTORDER
    # ============================================
    
    print("=" * 70)
    print("POSTORDER (Hijos → Raíz)")
    print("=" * 70)
    print()
    
    post_dir = arbol1.postorder_directo()
    post_func = arbol1.postorder_funcional()
    post_mut = arbol1.postorder_mutua()
    
    print("Versiones de POSTORDER:")
    print(f"  Directo (loop):      {post_dir}")
    print(f"  Funcional (reduce):  {post_func}")
    print(f"  Mutua (recursión):   {post_mut}")
    print()
    
    print("Verificación:")
    todas_iguales = post_dir == post_func == post_mut
    print(f"  {'✓ Todas iguales' if todas_iguales else '✗ Diferentes'}")
    print(f"  Esperado: ['E', 'B', 'C', 'D', 'A']")
    print()
    
    print("Explicación del orden:")
    print("  1. Proceso subárbol B:")
    print("     1.1. Proceso subárbol E:")
    print("          1.1.1. E es hoja → Visito E")
    print("     1.2. Visito B")
    print("  2. Proceso subárbol C:")
    print("     2.1. C es hoja → Visito C")
    print("  3. Proceso subárbol D:")
    print("     3.1. D es hoja → Visito D")
    print("  4. Visito A (raíz al final)")
    print()
    
    # ============================================
    # EJERCICIO 2: BFS
    # ============================================
    
    print("=" * 70)
    print("BFS (Por niveles)")
    print("=" * 70)
    print()
    
    bfs_orig = arbol1.bfs_original()
    bfs_iter = arbol1.bfs()
    bfs_rec = arbol1.bfs_recursivo()

    print("Versiones de BFS:")
    print(f"  Original (doc):      {bfs_orig}")
    print(f"  Iterativo:           {bfs_iter}")
    print(f"  Recursivo:           {bfs_rec}")
    print()
    
    print("Verificación:")
    todas_iguales = bfs_orig == bfs_iter == bfs_rec
    print(f"  {'✓ Todas iguales' if todas_iguales else '✗ Diferentes'}")
    print(f"  Esperado: ['A', 'B', 'C', 'D', 'E']")
    print()
    
    print("Explicación del orden (por niveles):")
    print("  Nivel 0: A")
    print("  Nivel 1: B, C, D")
    print("  Nivel 2: E")
    print("  Concatenado: A, B, C, D, E")
    print()
    
    # ============================================
    # COMPARACIÓN DE RECORRIDOS
    # ============================================
    
    print("=" * 70)
    print("COMPARACIÓN DE TODOS LOS RECORRIDOS")
    print("=" * 70)
    print()
    
    print(f"Árbol: {repr(arbol1)}")
    print()
    print(f"PREORDER:  {pre_func}")
    print(f"POSTORDER: {post_dir}")
    print(f"BFS:       {bfs_iter}")
    print()
    
    # ============================================
    # ÁRBOL MÁS COMPLEJO
    # ============================================
    
    print("=" * 70)
    print("ÁRBOL MÁS COMPLEJO")
    print("=" * 70)
    print()
    
    # Construir:
    #         1
    #       / | \
    #      2  3  4
    #     /|  |  |\
    #    5 6  7  8 9
    
    raiz = ArbolN(1)
    
    n2 = ArbolN(2)
    n2.insertar_subarbol(ArbolN(5))
    n2.insertar_subarbol(ArbolN(6))
    
    n3 = ArbolN(3)
    n3.insertar_subarbol(ArbolN(7))
    
    n4 = ArbolN(4)
    n4.insertar_subarbol(ArbolN(8))
    n4.insertar_subarbol(ArbolN(9))
    
    raiz.insertar_subarbol(n2)
    raiz.insertar_subarbol(n3)
    raiz.insertar_subarbol(n4)
    
    print("Árbol:")
    print(raiz)
    
    print("Recorridos:")
    print(f"  PREORDER:  {raiz.preorder_imperativo()}")
    print(f"  POSTORDER: {raiz.postorder_directo()}")
    print(f"  BFS:       {raiz.bfs()}")
    print()
    
    print("Esperados:")
    print(f"  PREORDER:  [1, 2, 5, 6, 3, 7, 4, 8, 9]")
    print(f"  POSTORDER: [5, 6, 2, 7, 3, 8, 9, 4, 1]")
    print(f"  BFS:       [1, 2, 3, 4, 5, 6, 7, 8, 9]")
    print()
    
    # ============================================
    # RESUMEN
    # ============================================
    
    print("=" * 70)
    print("RESUMEN DEL ALGORITMO")
    print("=" * 70)
    print("""
Pasos para verificar igualdad:

1. Verificar tipo (isinstance)
   └─ Si no es ArbolN → False

2. Comparar datos
   └─ Si datos diferentes → False

3. Comparar cantidad de subárboles
   └─ Si cantidades diferentes → False

4. Comparar cada subárbol RECURSIVAMENTE
   └─ Si algún par es diferente → False

5. Si pasó todas las pruebas → True

COMPLEJIDAD: O(n) donde n es la cantidad de nodos
(visitamos cada nodo una vez)
    """)