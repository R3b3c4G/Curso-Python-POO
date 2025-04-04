"""
Nombre: Rebeca Gregorio Espina.
Fecha: 3 de marzo de 2025
Descripión:
Se desea desarrollar un sistema en Python para gestionar un torneo de fútbol en el que participan
varios equipos, y cada equipo está compuesto por jugadores.

2. Gestionar Equipos:
    Cada equipo tiene un nombre, un ID único (generado automáticamente) y una lista de jugadores.
    Los equipos pueden agregar o remover jugadores, ya sea individualmente o en grupos.
    Los atributos de los equipos deben estar protegidos, y se debe controlar el acceso a ellos mediante
    métodos de acceso. Cada equipo debe poder calcular el total de goles anotados por todos sus jugadores.
Un Equipo está compuesto por varios Jugadores (relación de agregación).
"""

from Jugador import Jugador

class Equipo:
    no_id = 1

    def __init__(self, nombre:str, *jugadores:tuple[Jugador]):
        self._nombre = nombre
        self._jugadores = list(jugadores)
        self._id_equipo = Equipo.no_id
        Equipo.no_id += 1

    @property
    def id_equipo(self)-> int:
        """
        Getter para id_equipo.
        """
        return self._id_equipo

    @property
    def jugadores(self)-> list[Jugador]:
        """
        Getter para id_equipo.
        """
        return self._jugadores

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

    def agregar_jugadores(self, *jugadores:tuple[Jugador])-> None:
        for jugador in list(jugadores):
            if jugador not in self._jugadores:
                self._jugadores.append(jugador)
            else:
                print(f"{jugador.nombre} ya está en el equipo.")

    def remover_jugadores(self, *jugadores:tuple[Jugador])-> None:
        # Falta remover en grupos
        for jugador in jugadores:
            if jugador in self._jugadores:
                self._jugadores.remove(jugador)
            else:
                print(f"{jugador.nombre} no se encuentra en el equipo.")

    def mostrar_jugadores(self)-> None:
        if not self._jugadores:
            print("No hay jugadores.")
        else:
            print(f"Jugadores del equipo: {self._id_equipo}")
            for jugador in self._jugadores:
                print(jugador)

    def total_goles(self)-> int:
        contador = 0
        for jugador in self._jugadores:
            contador += jugador.goles
        return contador

    def __str__(self) -> str:
       jugadores = ", ".join(str(jugador) for jugador in self._jugadores)
       return f"Torneo(Nombre: {self._nombre}, id= {self._id_equipo}, jugadores: ({jugadores})"

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    """
    Función principal para la clase Equipo.
    """

