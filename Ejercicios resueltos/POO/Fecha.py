class Fecha:

    __slots__ = ("dia", "mes", "anio")

    def __init__(self, dia: int, mes: int, anio: int):
        self._validar(dia, mes, anio)
        self.dia = dia
        self.mes = mes
        self.anio = anio

    # ---------- Validación ----------
    @staticmethod
    def _es_bisiesto(anio: int) -> bool:
        return anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0)

    @classmethod
    def _dias_en_mes(cls, mes: int, anio: int) -> int:
        if mes == 2:
            return 29 if cls._es_bisiesto(anio) else 28
        if mes in (4, 6, 9, 11):
            return 30
        return 31

    @classmethod
    def _validar(cls, dia: int, mes: int, anio: int):
        if anio == 0:
            raise ValueError("El año 0 no existe en el calendario gregoriano.")
        if not (1 <= mes <= 12):
            raise ValueError("Mes fuera de rango (1-12).")
        max_dia = cls._dias_en_mes(mes, anio)
        if not (1 <= dia <= max_dia):
            raise ValueError(f"Dia fuera de rango (1-{max_dia}) para mes {mes} y año {anio}.")

    # ---------- Representación ----------
    def __str__(self) -> str:
        # Formato DD/MM/AAAA con ceros a la izquierda
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio:04d}"

    def __repr__(self) -> str:
        return f"Fecha({self.dia}, {self.mes}, {self.anio})"

    # ---------- Comparaciones ----------
    def _como_tuple(self):
        # Tupla ordenable (anio, mes, dia)
        return (self.anio, self.mes, self.dia)

    def es_mayor_que(self, otra: "Fecha") -> bool:
        if not isinstance(otra, Fecha):
            raise TypeError("Comparación sólo permitida con otra instancia de Fecha.")
        return self._como_tuple() > otra._como_tuple()

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Fecha):
            return NotImplemented
        return self._como_tuple() > other._como_tuple()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fecha):
            return NotImplemented
        return self._como_tuple() == other._como_tuple()


# Ejemplo de uso rápido (elimine o comente para producción):
if __name__ == "__main__":
    f1 = Fecha(15, 9, 2024)
    f2 = Fecha(1, 1, 2025)
    print(f1, ">", f2, "?", f1 > f2)
    print(f2, "es mayor que", f1, "?", f2.es_mayor_que(f1))
    print(f2>f1)