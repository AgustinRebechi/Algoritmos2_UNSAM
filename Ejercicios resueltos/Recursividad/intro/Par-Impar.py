def es_par(n: int) -> bool:
    return n == 0 or es_impar(n - 1)

def es_impar(n: int) -> bool:
    return False if n == 0 else es_par(n - 1)

def mostrar_paridad(n: int) -> None:
    n = abs(n)
    if es_par(n):
        print(f'{n} es par')
    else:
        print(f'{n} es impar')

mostrar_paridad(10)
mostrar_paridad(-10)