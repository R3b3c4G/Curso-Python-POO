"""
Nombre: Rebeca Gregorio Espina.
Fecha: 3 de marzo de 2025
Descripión:
Se desea desarrollar un sistema en Python para gestionar un torneo de fútbol en el que participan
varios equipos, y cada equipo está compuesto por jugadores.

1. Gestionar Jugadores:
    Cada jugador tiene un nombre, un número y una cantidad de goles anotados.
    Los jugadores pueden anotar goles, y el sistema debe actualizar su contador de goles.
    Los atributos de los jugadores deben estar protegidos, y se debe controlar el acceso a ellos mediante
    métodos de acceso.
"""
class Jugador:
    """
    Clase que representa a un jugador de fútbol.
    Sus atributos son: Nombre, número y goles(protegido).
    Sus métodos son: __init__(), __str__(), getter y setter del atributo protegido, nombre(), numero() y goles()
    """
    def __init__(self, nombre:str, numero:int, goles:int=0):
        """
        Constructor del Jugador.
        :param nombre: Nombre del jugador.
        :param numero: Número del jugador.
        :param goles: Cantidad inicial de goles, por defecto 0.
        """
        self._nombre = nombre
        self._numero = numero
        self._goles = goles

    @property
    def nombre(self)-> str:
        """
        Getter para nombre.
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre:str)-> None:
        """
        Setter para nombre.
        """
        self._nombre = nombre

    @property
    def numero(self)-> int:
        """
        Getter para numero.
        """
        return self._numero

    @numero.setter
    def numero(self, numero:int)-> None:
        """
        Setter para numero.
        """
        self._numero = numero

    @property
    def goles(self)-> int:
        """
        Getter para goles.
        """
        return self._goles

    @goles.setter
    def goles(self, goles:int)-> None:
        """
        Setter para goles.
        """
        self._goles = goles

    def anotar_goles(self, no_goles:int)-> None:
        """
        Incrementa la cantidad de goles anotados por el jugador.
        :param no_goles: Cantidad de goles a añadir.
        :return: No devuelve.
        """
        self._goles += no_goles

    def __str__(self)-> str:
        """
        Devuelve una representación en cadena del objeto.
        :return: Objeto en forma de cadena
        """
        return f"Información del jugador(nombre={self._nombre}, numero={self._numero}, goles={self._goles})"


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    """
    Función principal para la clase Jugador.
    """
