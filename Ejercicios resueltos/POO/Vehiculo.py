class Vehiculo:
    def __init__(self, marca: str, modelo: str, precio_base: float):
        self.marca = marca
        self.modelo = modelo
        self.precio_base = float(precio_base)

    def calcularCostoAlquiler(self, dias: int) -> float:
        if dias < 0:
            raise ValueError("La cantidad de días no puede ser negativa.")
        return self.precio_base * dias

    def __repr__(self):
        return f"{self.__class__.__name__}(marca={self.marca!r}, modelo={self.modelo!r}, precio_base={self.precio_base})"


class Auto(Vehiculo):
    """
    Subclase de Vehiculo que representa un auto.
    Incrementa en un 20% el costo de alquiler estándar.
    """
    def calcularCostoAlquiler(self, dias: int) -> float:
        costo_base = super().calcularCostoAlquiler(dias)
        return costo_base * 1.20


class Moto(Vehiculo):
    """
    Subclase de Vehiculo que representa una moto.
    Aplica un descuento del 15% sobre el costo de alquiler estándar.
    """
    def calcularCostoAlquiler(self, dias: int) -> float:
        costo_base = super().calcularCostoAlquiler(dias)
        return costo_base * 0.85


# Ejemplo de uso rápido
if __name__ == "__main__":
    vehiculo = Vehiculo("Genérica", "Base", 1000)
    auto = Auto("Ford", "Fiesta", 1500)
    moto = Moto("Yamaha", "FZ", 800)

    dias = 5
    print(f"Costo Vehiculo ({dias} días): {vehiculo.calcularCostoAlquiler(dias)}")
    print(f"Costo Auto ({dias} días): {auto.calcularCostoAlquiler(dias)}")
    print(f"Costo Moto ({dias} días): {moto.calcularCostoAlquiler(dias)}")