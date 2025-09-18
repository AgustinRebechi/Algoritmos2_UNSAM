from typing import Union
from collections.abc import Callable

Numerico = Union[int, float]

def wrapper(f: Callable, *args: Numerico, **kwargs: Numerico):
    print(f"Ejecutado {f.__name__} con argumentos {args} y {kwargs}")
    return f(*args, **kwargs)

def suma(a: int, b: int) -> Numerico:
    return a + b

def potencia(base: int, exp: int, mod: int = None) -> int:
    return pow(base, exp, mod) if mod else pow(base, exp)


print(wrapper(suma, 2,3))
print(wrapper(suma, a=24, b=1))

print(wrapper(potencia, 2, 3))
print(wrapper(potencia, 2, 3, mod=5)) 