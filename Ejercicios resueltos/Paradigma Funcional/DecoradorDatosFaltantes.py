from __future__ import annotations
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")
R = TypeVar("R")

def acepta_no_valor(func: Callable[[T], R]) -> Callable[[T | None], R | None]:
    """
    Decora una función de un único parámetro no nulo para que:
    - Si recibe None, devuelva None.
    - En caso contrario, evalúe la función original.

    Tipos:
      func: Callable[[T], R]
      return: Callable[[T | None], R | None]
    """
    @wraps(func)
    def wrapper(arg: T | None) -> R | None:
        if arg is None:
            return None
        return func(arg)
    return wrapper


# Ejemplo de uso mínimo:
if __name__ == "__main__":
    
    @acepta_no_valor
    def inverso(x: float) -> float:
        return 1 / x

    assert inverso(None) is None
    assert inverso(2.0) == 0.5