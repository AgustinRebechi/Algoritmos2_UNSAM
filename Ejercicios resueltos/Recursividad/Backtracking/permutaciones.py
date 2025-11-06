def permutacion(lista: list[int]) -> int:

    resultado = []

    def backtrack(actual: list[int], restantes: list[int]) -> None:

        # Caso base

        if len(restantes) == 0:
            resultado.append(actual.copy())
            return
        
        # Caso recursivo

        for i in range(len(restantes)):

            # Paso 1: Elegir un elemento

            elemento = restantes[i]

            # Paso 2: Agregarlo a una solucion parcial

            actual.append(elemento)

            # Paso 3: Crear una nueva lista sin este elemento

            nuevos_restantes = restantes[:i] + restantes[i+1:]

            # Paso 4: recursioon

            backtrack(actual, nuevos_restantes)

            # Paso 5: Backtrack

            actual.pop()
    backtrack([], lista)
    return resultado
    
print(permutacion([1, 2, 3]))