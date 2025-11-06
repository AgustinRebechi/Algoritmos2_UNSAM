def resta_lista(xs: list[int]) -> int:
    def apilado(xs: list[int], pila: list[int]):
        if xs != []:
            pila.append(xs[0])
            apilado(xs[1:], pila)

    def desapilado(pila: list[int], acumulador: int) -> int:
        if pila == []:
            return acumulador
        else:
            return desapilado(pila, pila.pop() - acumulador)
      
    pila = []
    apilado(xs, pila)
    return desapilado(pila, 0)

def resta_lista_iterativa(xs):

    # Paso 1: Apilar todos los elementos
    pila = []
    for elemento in xs:
        pila.append(elemento)
    
    # Paso 2: Desapilar y calcular
    resultado = 0
    while len(pila) > 0:
        resultado = pila.pop() - resultado
    
    return resultado

def suma_resta_alternada_cola(lista, acumulador=0, es_suma=True):
    if lista == []:
        return acumulador
    else:
        # Calculamos ANTES de la llamada recursiva
        if es_suma:
            nuevo_acum = acumulador + lista[0]
        else:
            nuevo_acum = acumulador - lista[0]
        
        # Llamada recursiva con el acumulador ya actualizado
        return suma_resta_alternada_cola(lista[1:], nuevo_acum, not es_suma)

print(resta_lista([10, 2, 5, 9])) # (10 - (2 - (5 - 9)) = 12)
print(resta_lista_iterativa([10, 2, 5, 9])) # (10 - (2 - (5 - 9)) = 12)
print(suma_resta_alternada_cola([1, 2, 3, 4, 5]))  # Output: -1 