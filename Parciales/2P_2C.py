from typing import List, Optional

class Empleado:
    def __init__(self, nombre: str, antiguedad: int = 0, hijos: Optional[int] = 0):
        self.nombre = nombre
        self.antiguedad = antiguedad
        self.hijos_a_cargo: List[Empleado] = []
        self.hijos = hijos  # cantidad de hijos personales (para bono)

    def agregar_subordinado(self, empleado: "Empleado"):
        self.hijos_a_cargo.append(empleado)

    def calcular_sueldo(self) -> int:
        # se redefine en subclases
        return 0

    def calcular_sueldo_total(self) -> int:
        total = self.calcular_sueldo()
        for sub in self.hijos_a_cargo:
            total += sub.calcular_sueldo_total()
        return total

    def tiene_bono(self) -> bool:
        return self.hijos > 0

class DirectorArea(Empleado):
    def calcular_sueldo(self) -> int:
        sueldo = 2_500_000 + 5_000 * self.antiguedad
        if self.tiene_bono():
            sueldo += 100_000
        return sueldo


class LiderTecnico(Empleado):
    def calcular_sueldo(self) -> int:
        sueldo = 100_000 + 3_000 * self.antiguedad
        if self.tiene_bono():
            sueldo += 100_000
        return sueldo


class Desarrollador(Empleado):
    pass


class DesarrolladorSenior(Desarrollador):
    def calcular_sueldo(self) -> int:
        sueldo = 700_000 + 2_000 * self.antiguedad
        if self.tiene_bono():
            sueldo += 100_000
        return sueldo


class DesarrolladorJunior(Desarrollador):
    def calcular_sueldo(self) -> int:
        sueldo = 500_000 + 1_500 * self.antiguedad
        if self.tiene_bono():
            sueldo += 100_000
        return sueldo


class DesarrolladorTrainee(Desarrollador):
    def calcular_sueldo(self) -> int:
        sueldo = 300_000
        if self.tiene_bono():
            sueldo += 100_000
        return sueldo


class Pasante(Empleado):
    def calcular_sueldo(self) -> int:
        return 0

class Organigrama:
    def __init__(self, director_general: Empleado):
        self.director_general = director_general

    def calcular_sueldo_total(self) -> int:
        total = 0
        for sub in self.director_general.hijos_a_cargo:
            total += sub.calcular_sueldo_total()
        return total

    def es_valido(self) -> bool:
        # Validación recursiva: el organigrama tiene la estructura correcta
        def validar(empleado: Empleado) -> bool:
            if isinstance(empleado, DirectorArea):
                if empleado.__class__.__name__ == "DirectorArea" and empleado.nombre == "IT":
                    # debe tener líderes técnicos
                    if not all(isinstance(e, LiderTecnico) for e in empleado.hijos_a_cargo):
                        return False
                # RRHH o Finanzas no deben tener más directores
            elif isinstance(empleado, LiderTecnico):
                # los líderes deben tener desarrolladores
                if not any(isinstance(e, Desarrollador) for e in empleado.hijos_a_cargo):
                    return False
            elif isinstance(empleado, DesarrolladorSenior):
                # un senior puede tener pasantes, otros devs no
                for e in empleado.hijos_a_cargo:
                    if not isinstance(e, Pasante):
                        return False
            elif isinstance(empleado, DesarrolladorJunior) or isinstance(empleado, DesarrolladorTrainee):
                # estos no deben tener subordinados
                if empleado.hijos_a_cargo:
                    return False
            elif isinstance(empleado, Pasante):
                # no deben tener subordinados
                if empleado.hijos_a_cargo:
                    return False

            # validar hijos recursivamente
            return all(validar(h) for h in empleado.hijos_a_cargo)

        return validar(self.director_general)

def main():
    # Crear estructura válida
    dg = Empleado("Director General")

    dir_it = DirectorArea("IT", antiguedad=5)
    dir_fin = DirectorArea("Finanzas", antiguedad=10)
    dir_rrhh = DirectorArea("RRHH", antiguedad=3)

    dg.agregar_subordinado(dir_it)
    dg.agregar_subordinado(dir_fin)
    dg.agregar_subordinado(dir_rrhh)

    lider1 = LiderTecnico("Líder A", antiguedad=4)
    dir_it.agregar_subordinado(lider1)

    dev1 = DesarrolladorSenior("Dev Senior", antiguedad=6, hijos=1)
    dev2 = DesarrolladorJunior("Dev Junior", antiguedad=2)
    dev3 = DesarrolladorTrainee("Dev Trainee", antiguedad=0)
    lider1.agregar_subordinado(dev1)
    lider1.agregar_subordinado(dev2)
    lider1.agregar_subordinado(dev3)

    pas = Pasante("Pasante X")
    dev1.agregar_subordinado(pas)

    org_valido = Organigrama(dg)
    print("Organigrama válido:", org_valido.es_valido())
    print("Sueldo total:", org_valido.calcular_sueldo_total())

    # Organigrama inválido
    dg_invalido = Empleado("Director General")
    dir_it2 = DirectorArea("IT")
    dev_raro = DesarrolladorJunior("Dev Junior sin líder")
    dir_it2.agregar_subordinado(dev_raro)
    dg_invalido.agregar_subordinado(dir_it2)
    org_invalido = Organigrama(dg_invalido)
    print("Organigrama inválido:", org_invalido.es_valido())
    
if __name__ == "__main__":
    main()