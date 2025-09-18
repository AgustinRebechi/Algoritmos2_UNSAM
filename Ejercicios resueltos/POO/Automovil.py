from dataclasses import dataclass, field
from datetime import date
from typing import Dict, Any, Optional

class PermisoError(Exception):
    """Error relacionado con emisión de permisos."""


class AutorizacionError(Exception):
    """Error relacionado con la autorización del camión."""


@dataclass
class Automovil:
    patente: str
    habilitado: bool = field(default=False, init=False)
    fecha_permiso: Optional[date] = field(default=None, init=False)

    def esta_habilitado(self) -> bool:
        return self.habilitado

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} patente={self.patente} habilitado={self.habilitado}>"


class AutoMediano(Automovil):
    def adquirir_permiso(self, fecha: date) -> None:
        """Otorga el permiso y habilita el auto mediano."""
        if self.habilitado:
            return
        self.fecha_permiso = fecha
        self.habilitado = True


@dataclass
class Camion(Automovil):
    peso_maximo: int  # kg
    cantidad_ejes: int
    concesionaria: "ConcesionariaCamiones"
    autorizado: bool = field(default=False, init=False)

    def solicitar_autorizacion(self) -> bool:
        """Solicita a la concesionaria la autorización previa."""
        if self.autorizado:
            return True
        self.autorizado = self.concesionaria.autorizar(self)
        return self.autorizado

    def adquirir_permiso(self, fecha: date) -> None:
        """Sólo posible si previamente fue autorizado por la concesionaria."""
        if not self.autorizado:
            raise AutorizacionError("El camión no está autorizado por la concesionaria.")
        if self.habilitado:
            return
        self.fecha_permiso = fecha
        self.habilitado = True


class ConcesionariaCamiones:
    def __init__(self, nombre: str):
        self.nombre = nombre
        # patente -> datos verificados
        self._registro: Dict[str, Dict[str, Any]] = {}

    def verificar_caracteristicas(self, camion: Camion) -> bool:
        """Reglas simples de validación (pueden extenderse)."""
        if camion.peso_maximo <= 0:
            return False
        if not (2 <= camion.cantidad_ejes <= 8):
            return False
        # Ejemplo de límite regulatorio arbitrario
        if camion.peso_maximo > 52000:
            return False
        return True

    def autorizar(self, camion: Camion) -> bool:
        """Verifica y registra el camión si cumple requisitos."""
        if camion.patente in self._registro:
            # Ya registrado -> se considera autorizado
            return True
        if not self.verificar_caracteristicas(camion):
            return False
        self._registro[camion.patente] = {
            "peso_maximo": camion.peso_maximo,
            "cantidad_ejes": camion.cantidad_ejes,
            "autorizado_en": date.today(),
        }
        return True

    def datos_camion(self, patente: str) -> Optional[Dict[str, Any]]:
        return self._registro.get(patente)

    def __repr__(self) -> str:
        return f"<ConcesionariaCamiones {self.nombre} registrados={len(self._registro)}>"