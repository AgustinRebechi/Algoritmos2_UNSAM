from __future__ import annotations
from typing import Union

Number = Union[int, float]


class Punto:
    __slots__ = ("_x", "_y")

    def __init__(self, x: Number = 0.0, y: Number = 0.0) -> None:
        self._x = float(x)
        self._y = float(y)

    # Métodos de asignación
    def set_x(self, x: Number) -> None:
        self._x = float(x)

    def set_y(self, y: Number) -> None:
        self._y = float(y)

    def set_xy(self, x: Number, y: Number) -> None:
        self._x = float(x)
        self._y = float(y)

    # Métodos de acceso
    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    # Suma con otro punto
    def sumar(self, otro: "Punto") -> "Punto":
        if not isinstance(otro, Punto):
            raise TypeError("La suma requiere otro Punto")
        return Punto(self._x + otro._x, self._y + otro._y)

    # Operador +
    def __add__(self, otro: "Punto") -> "Punto":
        return self.sumar(otro)

    # Igualdad
    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, Punto):
            return False
        return self._x == otro._x and self._y == otro._y

    def __repr__(self) -> str:
        return f"Punto(x={self._x}, y={self._y})"


if __name__ == "__main__":
    a = Punto(1.5, 2.5)
    b = Punto(3, -0.5)
    c = a + b
    print(a, b, c)
    print("c == Punto(4.5, 2.0)?", c == Punto(4.5, 2.0))