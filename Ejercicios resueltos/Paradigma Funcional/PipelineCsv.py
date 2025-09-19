from collections.abc import Iterator

def leer_lineas(ruta_archivo: str) -> Iterator[str]:
    
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            yield linea.strip()


def parsear_campos(lineas: Iterator[str]) -> Iterator[list[str]]:
    for linea in lineas:
        yield linea.split(",")


def dicts(campos: Iterator[list[str]], columnas: list[str]) -> Iterator[dict[str, str]]:
    for fila in campos:
        yield dict(zip(columnas, fila))


def sepal_width_setosa(filas: Iterator[dict[str, str]]) -> Iterator[float]:
    for fila in filas:
        if fila["species"] == "Iris-setosa":
            yield float(fila["sepal_width"])


if __name__ == "__main__":
    ruta = "Ejercicios resueltos\Paradigma Funcional\IRIS.csv"
    columnas = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

    lineas = leer_lineas(ruta)
    campos = parsear_campos(lineas)
    filas = dicts(campos, columnas)

    # --- Suma ---
    suma = sum(sepal_width_setosa(filas))
    print("Suma sepal_width Iris-setosa:", suma)  # esperado: 170.9

    # --- Promedio ---
    # Tenemos que recrear el pipeline porque los generadores se agotan
    lineas = leer_lineas(ruta)
    campos = parsear_campos(lineas)
    filas = dicts(campos, columnas)

    valores = list(sepal_width_setosa(filas))
    promedio = sum(valores) / len(valores)
    print("Promedio sepal_width Iris-setosa:", promedio)  # esperado: 3.418

