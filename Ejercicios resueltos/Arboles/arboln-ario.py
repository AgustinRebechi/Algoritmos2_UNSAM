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