from pymonad.tools import curry
from typing import Callable
from functools import partial

@curry(2)
def log(tipo: str, mensaje: str) -> str:
    """
    Función que registra un mensaje de log con un tipo específico.
    :param tipo: Tipo de log (e.g., "info", "error").
    :param mensaje: Mensaje a registrar.

    :return: Mensaje de log formateado. 
    """

    formatted_message: str = f"[{tipo.upper()}] {mensaje}"

    print(formatted_message)
    return formatted_message

def log_lambda(tipo: str) -> Callable[[str], str]:
    """
    Función log currificada usando lambda

    :param tipo: Tipo de log (e.g., "info", "error").
    :return: Función que toma un mensaje y registra el log. 

    """
    return lambda mensaje: print(f"[{tipo.upper()}] {mensaje}") or f"[{tipo.upper()}] {mensaje}"

def log_curry_partial(tipo: str) -> Callable[[str], str]:
    """
    Función log currificada usando funcpartial de pymonad

    :param tipo: Tipo de log (e.g., "info", "error").
    :return: Función que toma un mensaje y registra el log.

    """

    return partial(log, tipo)

if __name__ == "__main__":

    # curry

    print("\nUsando log curry:\n")

    log_info: Callable[[str], str] = log("info")
    log_error: Callable[[str], str] = log("error")

    log_info("Este es un mensaje informativo.")
    log_error("Este es un mensaje de error.")

    # funcpartials
    
    print("\nUsando log funcpartial:\n")
    log_error_partial = log_curry_partial("error")
    log_info_partial = log_curry_partial("información")
    
    log_error_partial("Error de validación")
    log_info_partial("Datos guardados correctamente")

    # lambda

    print("\nUsando log_lambda:\n")
    log_info_lambda = log_lambda("info")
    log_error_lambda = log_lambda("error")

    log_info_lambda("Este es un mensaje informativo usando lambda.")
    log_error_lambda("Este es un mensaje de error usando lambda.")