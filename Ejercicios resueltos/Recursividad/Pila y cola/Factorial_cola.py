def factorial(n: int) -> int:
    def factorial_interna(n: int, acumulador: int) -> int:
        if n <= 1:
            return acumulador
        else:
            return factorial_interna(n-1, acumulador * n)
    return factorial_interna(n, 1)

print(factorial(3))  # Output: 6