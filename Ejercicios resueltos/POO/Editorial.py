class Publicacion:
    def __init__(self, titulo: str, precio: float):
        self.titulo = titulo
        self.precio = float(precio)

    def actualizar_precio(self, nuevo_precio: float):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = float(nuevo_precio)

    def __str__(self):
        return f"{self.__class__.__name__}: '{self.titulo}' - Precio: ${self.precio:,.2f}"


class Libro(Publicacion):
    def __init__(self, titulo: str, precio: float, paginas: int, anio_publicacion: int):
        super().__init__(titulo, precio)
        self.paginas = int(paginas)
        self.anio_publicacion = int(anio_publicacion)

    def __str__(self):
        return (f"Libro: '{self.titulo}' ({self.anio_publicacion}) - "
                f"{self.paginas} págs - Precio: ${self.precio:,.2f}")


class Disco(Publicacion):
    def __init__(self, titulo: str, precio: float, duracion_min: int):
        super().__init__(titulo, precio)
        self.duracion_min = int(duracion_min)

    def __str__(self):
        return (f"Disco: '{self.titulo}' - Duración: {self.duracion_min} min - "
                f"Precio: ${self.precio:,.2f}")


def main():
    publicaciones = [
        Libro("Introducción a Algoritmos", 15000, 520, 2022),
        Disco("Clásicos del Rock", 8900, 74),
        Libro("Python Profesional", 21000, 680, 2024),
        Disco("Música Ambiental", 7600, 55)
    ]

    print("Listado de publicaciones:")
    for p in publicaciones:
        print(" -", p)

    total = sum(p.precio for p in publicaciones)
    promedio = total / len(publicaciones)
    print(f"\nTotal catálogo: ${total:,.2f}")
    print(f"Precio promedio: ${promedio:,.2f}")

    # Ejemplo de actualización de precio
    publicaciones[0].actualizar_precio(15500)
    print("\nTras actualizar precio del primer libro:")
    print(" -", publicaciones[0])


if __name__ == "__main__":
    main()