from typing import List

def desde_hasta(desde: int, hasta: int) -> List[int]:
    if desde > hasta:
        return []
    return [desde] + desde_hasta(desde + 1, hasta)

print(desde_hasta(3, 7))  
def sumatoria(n: int) -> int:
    return sum(desde_hasta(1, n))

print(sumatoria(5))

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(3)) 