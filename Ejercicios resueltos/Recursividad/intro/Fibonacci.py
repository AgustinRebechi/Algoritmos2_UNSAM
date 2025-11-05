def fibonacci(n: int) -> int:
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
for i in range(10):
    print(fibonacci(i))

# Optimización con memoización

def fibonacci_memo(n, memo={}):
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

for i in range(10):
    print(fibonacci_memo(i))