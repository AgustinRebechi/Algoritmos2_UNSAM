def factorial(n: int) -> int:
    solucion = 1
    while n > 1:
        solucion *= n
        n -= 1
    return solucion

print(factorial(3))  # Output: 6