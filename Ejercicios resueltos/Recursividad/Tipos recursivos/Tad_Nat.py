from typing import Union, TypeAlias

# tipos y clases

Nat: TypeAlias = Union["Cero", "Suc"]

class Cero:
    def __repr__(self):
        return 'Cero'

class Suc:
    def __init__(self, pred: Nat):
        self.pred = pred

    def __repr__(self):
        if isinstance(self.pred, Cero):
            return 'Suc(Cero)'
        else:
            return f'Suc({self.pred.__repr__()})'

# Constructores

def cero() -> Nat:
    return Cero()

def suc(n: Nat) -> Nat:
    return Suc(n)

# Proyectoras

def es_cero(n: Nat) -> bool:
    return isinstance(n, Cero)

def pred(n: Nat) -> Nat:
    if es_cero(n):
        raise ValueError('cero no tiene predecesor')
    else:
        return n.pred
    
# Conversion

def nat_to_int(n: Nat) -> int:
    if es_cero(n):
        return 0
    else:
        return 1 + nat_to_int(pred(n))
    
def int_to_nat(n: int) -> Nat:
    if n == 0:
        return cero()
    else:
        return suc(int_to_nat(n - 1))
    
# Operaciones

def suma(x: Nat, y: Nat) -> Nat:
    if es_cero(x):
        return y
    else:
        return suma(pred(x), suc(y))

def resta(x: Nat, y: Nat) -> Nat:
    if es_cero(y):
        return x
    elif es_cero(x):
        return cero()  # No podemos tener negativos
    else:
        return resta(pred(x), pred(y))

def multiplicacion(x: Nat, y: Nat) -> Nat:
    if es_cero(x) or es_cero(y):
        return cero()
    else:
        return suma(y, multiplicacion(pred(x), y))
    
def factorial(n: Nat) -> Nat:
    if es_cero(n):
        return suc(cero())  # 0! = 1
    else:
        return multiplicacion(n, factorial(pred(n)))
    
def potencia(x: Nat, y: Nat) -> Nat:
    """Calcula x elevado a la y: x^y
    Estrategia: x^y = x * x * x * ... (y veces)"""
    if es_cero(y):
        return suc(cero())  # Cualquier número^0 = 1
    else:
        return multiplicacion(x, potencia(x, pred(y)))

# Comparacion

def igual(x: Nat, y: Nat) -> bool:
    if es_cero(x) and es_cero(y):
        return True
    elif es_cero(x) or es_cero(y):
        return False
    else:
        return igual(pred(x), pred(y))

def menor_que(x: Nat, y: Nat) -> bool:
    if es_cero(x) and es_cero(y):
        return False
    elif es_cero(x):
        return True
    elif es_cero(y):
        return False
    else:
        return menor_que(pred(x), pred(y))

def mayor_que(x: Nat, y: Nat) -> bool:
    return menor_que(y, x)


if __name__ == "__main__":
    print("=== TAD Nat - Ejemplos ===\n")
    
    # Crear números
    n0 = cero()
    n3 = int_to_nat(3)
    n5 = int_to_nat(5)
    n2 = int_to_nat(2)
    
    print(f"n0 = {nat_to_int(n0)} -> {repr(n0)}")
    print(f"n3 = {nat_to_int(n3)} -> {repr(n3)}")
    print(f"n5 = {nat_to_int(n5)}")
    print(f"n2 = {nat_to_int(n2)}\n")
    
    # Suma
    resultado = suma(n3, n5)
    print(f"3 + 5 = {nat_to_int(resultado)}")
    
    # Resta
    resultado = resta(n5, n3)
    print(f"5 - 3 = {nat_to_int(resultado)}")
    
    # Multiplicación
    resultado = multiplicacion(n3, n5)
    print(f"3 * 5 = {nat_to_int(resultado)}")
    
    # Potencia
    resultado = potencia(n2, n3)
    print(f"2 ^ 3 = {nat_to_int(resultado)}")
    
    # Comparaciones
    print(f"3 == 5: {igual(n3, n5)}")
    print(f"3 < 5: {menor_que(n3, n5)}")
    print(f"5 > 3: {mayor_que(n5, n3)}")