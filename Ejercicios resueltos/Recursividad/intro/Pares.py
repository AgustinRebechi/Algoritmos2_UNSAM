from typing import List, Tuple

def pares_rec(n: int, a: int) -> List[Tuple[int, int]]:
    if a >= n // 2 + 1:
        return []
    b = n - a
    return [(a, b)] + pares_rec(n, a + 1)

def pares(n: int) -> List[Tuple[int, int]]:
    return pares_rec(n, 1)

print(pares(5))  # Ejemplo de uso