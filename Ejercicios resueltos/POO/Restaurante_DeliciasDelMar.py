class Restaurante:
    _total_sucursales = 0  # contador de instancias

    def __init__(self, nombre: str, ciudad: str, numero_empleados: int):
        self.nombre = nombre
        self.ciudad = ciudad
        self.numero_empleados = numero_empleados
        Restaurante._total_sucursales += 1

    @classmethod
    def obtener_numero_sucursales(cls) -> int:
        return cls._total_sucursales

    def calcular_costo_operativo(self, salario_promedio: float = 2000.0) -> float:
        return self.numero_empleados * salario_promedio

    def __str__(self):
        return f"{self.nombre} ({self.ciudad}) - Empleados: {self.numero_empleados}"


def main():
    # Crear sucursales
    sucursal_1 = Restaurante("Delicias del Mar San Martin Centro", "San Martin Centro", 12)
    sucursal_2 = Restaurante("Delicias del Mar Villa Ballester", "Villa Ballester", 18)
    sucursal_3 = Restaurante("Delicias del Mar San Martin Billingurst", "San Martin Billingurst", 10)

    sucursales = [sucursal_1, sucursal_2, sucursal_3]

    # Mostrar número total de sucursales
    print("Número total de sucursales:", Restaurante.obtener_numero_sucursales())

    # Calcular y mostrar costo operativo de cada sucursal
    for suc in sucursales:
        costo = suc.calcular_costo_operativo()  # usa salario promedio 2000
        print(f"Sucursal: {suc.nombre} | Ciudad: {suc.ciudad} | Empleados: {suc.numero_empleados} | Costo mensual: ${costo:,.2f}")


if __name__ == "__main__":
    main()