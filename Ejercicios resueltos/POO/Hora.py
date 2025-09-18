import typing

class Hora:

    __slots__ = ['__hora', '__minuto', '__segundo']

    def __init__(self, hora: int = 0, minuto: int = 0, segundo: int = 0):
        """Constructor de Hora.

        :param hora: Hora inicial (0-23).
        :type hora: int
        :param minuto: Minuto inicial (0-59).
        :type minuto: int
        :param segundo: Segundo inicial (0-59).
        :type segundo: int

        :returns: None
        :rtype: None

        :raises TypeError: si algún valor está fuera de rango.
        """
        # Validacion de la hora
        self.__validar(hora, minuto, segundo)
        # Constructor
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    # ------ Validación

    def __validar(self, hora: int, minuto: int, segundo: int) -> None:
        """ Validación de los valores de hora, minuto y segundo.

        :param hora: Hora (0-23).
        :type hora: int
        :param minuto: Minuto (0-59).
        :type minuto: int
        :param segundo: Segundo (0-59).
        :type segundo: int

        returns: None
        rtype: None

        raises: ValueError si algún valor está fuera de rango.
        """
        if not (0 <= hora < 24):
            raise ValueError("Hora fuera de rango (0-23).")
        if not (0 <= minuto < 60):
            raise ValueError("Minuto fuera de rango (0-59).")
        if not (0 <= segundo < 60):
            raise ValueError("Segundo fuera de rango (0-59).")
        
    # ------- Suma


    def __iadd__(self, otra: 'Hora') -> 'Hora':
        """ Suma otra instancia de Hora a la actual.

        :param otra: Otra instancia de Hora.
        :type otra: Hora
        :returns: La instancia actual modificada.
        :rtype: Hora

        :raises: TypeError si 'otra' no es una instancia de Hora.
        """

        if not isinstance(otra, Hora):
            raise TypeError("La suma solo es posible con otra instancia de Hora.")

        total_segundos = self.__segundo + otra.__segundo
        total_minutos = self.__minuto + otra.__minuto + total_segundos // 60
        total_horas = self.__hora + otra.__hora + total_minutos // 60

        self.__hora = total_horas % 24
        self.__minuto = total_minutos % 60
        self.__segundo = total_segundos % 60
        return self

    def __add__(self, other: 'Hora') -> 'Hora':
        """ Suma dos instancias de Hora y devuelve una nueva instancia.

        :param other: Otra instancia de Hora.
        :type other: Hora
        :returns: Nueva instancia de Hora
        con la suma.
        :rtype: Hora

        :raises: TypeError si 'other' no es una instancia de Hora.
        """
        if not isinstance(other, Hora):
            raise TypeError("La suma solo es posible con otra instancia de Hora.")

        total_segundos = self.__segundo + other.__segundo
        total_minutos = self.__minuto + other.__minuto + total_segundos // 60
        total_horas = self.__hora + other.__hora + total_minutos // 60

        nueva_hora = total_horas % 24
        nueva_minuto = total_minutos % 60
        nueva_segundo = total_segundos % 60
        
        return Hora(nueva_hora, nueva_minuto, nueva_segundo)
        
    # ------- Visualización

    def __str__(self) -> str:
        """ Representación en cadena de la hora en formato HH:MM:SS.

        :returns: Cadena con la representación de la hora.
        :rtype: str
        """
        return f"{self.__hora:02}:{self.__minuto:02}:{self.__segundo:02}"
    
    # ------ Getters

    @property
    def hora(self) -> int:
        """ Getter para la hora.

        :returns: La hora.
        :rtype: int
        """
        return self.__hora
    @property
    def minuto(self) -> int:
        """ Getter para el minuto.

        :returns: El minuto.
        :rtype: int
        """
        return self.__minuto
    @property
    def segundo(self) -> int:
        """ Getter para el segundo.

        :returns: El segundo.
        :rtype: int
        """
        return self.__segundo
    
    # ------ Setters

    @hora.setter
    def hora(self, valor: int) -> None:
        """ Setter para la hora.

        :param valor: Nueva hora (0-23).
        :type valor: int
        :returns: None
        :rtype: None

        :raises: ValueError si el valor está fuera de rango.
        """
        self.__validar(valor, self.__minuto, self.__segundo)
        self.__hora = valor
        
    @minuto.setter
    def minuto(self, valor: int) -> None:
        """ Setter para el minuto.

        :param valor: Nuevo minuto (0-59).
        :type valor: int
        :returns: None
        :rtype: None

        :raises: ValueError si el valor está fuera de rango.
        """
        self.__validar(self.__hora, valor, self.__segundo)
        self.__minuto = valor

    @segundo.setter
    def segundo(self, valor: int) -> None:
        """ Setter para el segundo.

        :param valor: Nuevo segundo (0-59).
        :type valor: int
        :returns: None
        :rtype: None

        :raises: ValueError si el valor está fuera de rango.
        """
        self.__validar(self.__hora, self.__minuto, valor)
        self.__segundo = valor


if __name__ == "__main__":
    hora = Hora()
    print(hora)  # Output: 00:00:00


    hora_suma = Hora(23,31,56) + Hora(1, 30, 45)
    print(hora_suma)  # Output: 01:02:41
    
    hora_base = Hora(23, 15, 30)
    hora_sumar = Hora(2, 45, 50)

    print(hora_base)
    hora_base += hora_sumar
    print(hora_base)    