from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod

# -----------------------------
# Modelo común
# -----------------------------

@dataclass(frozen=True)
class Trayecto:
    origen: str
    destino: str
    distancia_km: float          # distancia total en kilómetros
    cantidad_estaciones: int     # incluye terminales?

    def __post_init__(self):
        if self.distancia_km <= 0:
            raise ValueError("La distancia debe ser positiva")
        if self.cantidad_estaciones <= 0:
            raise ValueError("La cantidad de estaciones debe ser positiva")


# ============================================================
# (a) Especializando la clase Viaje según el tipo de viaje
# ============================================================

class Viaje:
    def __init__(self, trayecto: Trayecto, vagones: int, capacidad_maxima: int, pasajeros: int):
        if vagones <= 0:
            raise ValueError("La cantidad de vagones debe ser positiva")
        if capacidad_maxima <= 0:
            raise ValueError("La capacidad máxima debe ser positiva")
        if not (0 <= pasajeros <= capacidad_maxima):
            raise ValueError("Pasajeros fuera de rango")
        self.trayecto = trayecto
        self.vagones = vagones
        self.capacidad_maxima = capacidad_maxima
        self.pasajeros = pasajeros

    def tiempo_de_demora(self) -> float:
        raise NotImplementedError("Implementar en subclases")

    # Helper para reutilizar en fórmulas
    @property
    def distancia(self) -> float:
        return self.trayecto.distancia_km

    @property
    def estaciones(self) -> int:
        return self.trayecto.cantidad_estaciones


class ViajeDiesel(Viaje):
    # distancia * estaciones / 2 + (estaciones + pasajeros)/10
    def tiempo_de_demora(self) -> float:
        return (self.distancia * self.estaciones) / 2 + (self.estaciones + self.pasajeros) / 10


class ViajeElectrico(Viaje):
    # distancia * estaciones / 2
    def tiempo_de_demora(self) -> float:
        return (self.distancia * self.estaciones) / 2


class ViajeAltaVelocidad(Viaje):
    # distancia / 10
    def tiempo_de_demora(self) -> float:
        return self.distancia / 10


# ============================================================
# (b) Viaje sin especializar + TipoDeViaje (patrón Strategy)
# ============================================================

class TipoDeViaje(ABC):
    @abstractmethod
    def calcular_tiempo(self, trayecto: Trayecto, pasajeros: int) -> float:
        pass


class TipoDiesel(TipoDeViaje):
    def calcular_tiempo(self, trayecto: Trayecto, pasajeros: int) -> float:
        return (trayecto.distancia_km * trayecto.cantidad_estaciones) / 2 + (trayecto.cantidad_estaciones + pasajeros) / 10


class TipoElectrico(TipoDeViaje):
    def calcular_tiempo(self, trayecto: Trayecto, pasajeros: int) -> float:
        return (trayecto.distancia_km * trayecto.cantidad_estaciones) / 2


class TipoAltaVelocidad(TipoDeViaje):
    def calcular_tiempo(self, trayecto: Trayecto, pasajeros: int) -> float:
        return trayecto.distancia_km / 10


class ViajeConTipo:
    def __init__(self, trayecto: Trayecto, vagones: int, capacidad_maxima: int, pasajeros: int, tipo: TipoDeViaje):
        if vagones <= 0:
            raise ValueError("La cantidad de vagones debe ser positiva")
        if capacidad_maxima <= 0:
            raise ValueError("La capacidad máxima debe ser positiva")
        if not (0 <= pasajeros <= capacidad_maxima):
            raise ValueError("Pasajeros fuera de rango")
        self.trayecto = trayecto
        self.vagones = vagones
        self.capacidad_maxima = capacidad_maxima
        self.pasajeros = pasajeros
        self.tipo = tipo

    def tiempo_de_demora(self) -> float:
        return self.tipo.calcular_tiempo(self.trayecto, self.pasajeros)

    def cambiar_tipo(self, nuevo_tipo: TipoDeViaje):
        self.tipo = nuevo_tipo


# -----------------------------
# Ejemplo de uso
# -----------------------------
if __name__ == "__main__":
    tray = Trayecto("A", "B", distancia_km=300, cantidad_estaciones=5)

    # Variante (a)
    diesel = ViajeDiesel(tray, vagones=10, capacidad_maxima=800, pasajeros=500)
    electrico = ViajeElectrico(tray, vagones=10, capacidad_maxima=800, pasajeros=500)
    alta = ViajeAltaVelocidad(tray, vagones=8, capacidad_maxima=600, pasajeros=400)

    print("Variante (a):")
    print("Diesel:", diesel.tiempo_de_demora())
    print("Eléctrico:", electrico.tiempo_de_demora())
    print("Alta Velocidad:", alta.tiempo_de_demora())

    # Variante (b)
    viaje_tipo = ViajeConTipo(tray, vagones=10, capacidad_maxima=800, pasajeros=500, tipo=TipoDiesel())
    print("\nVariante (b):")
    print("Inicial Diesel:", viaje_tipo.tiempo_de_demora())
    viaje_tipo.cambiar_tipo(TipoElectrico())
    print("Cambiado a Eléctrico:", viaje_tipo.tiempo_de_demora())
    viaje_tipo.cambiar_tipo(TipoAltaVelocidad())
    print("Cambiado a Alta Velocidad:", viaje_tipo.tiempo_de_demora())