"""
Nombre: Rebeca Gregorio Espina.
Fecha: 3 de abril de 2025.
Descripión:
Se desea desarrollar un sistema en Python para gestionar un torneo de fútbol en el que participan
varios equipos, y cada equipo está compuesto por jugadores.

3. Gestionar Torneos:
    Cada torneo tiene un nombre y una lista de equipos participantes.
    Los torneos pueden agregar o remover equipos, ya sea individualmente o en grupos.
    El sistema debe permitir mostrar la lista de equipos participantes en el torneo.
    El sistema debe generar un rol de partidos estilo "todos contra todos", organizado por jornadas de todos los equipos
    participantes, donde cada jornada contenga un conjunto de partidos que no se solapen (es decir, ningún equipo juegue
    más de un partido por jornada).
Un Torneo está compuesto por varios Equipos (relación de agregación).
"""

from Equipo import Equipo
from Jugador import Jugador

class Torneo:
    """
    Clase que representa a un torneo de fútbol.
    Sus atributos son: nombre y equipos(protegido).
    Sus métodos son: __init__(), __str__(), getter y setter del atributo protegido, nombre() y equipos().
    """
    def __init__(self, nombre:str, *equipos:tuple[Equipo]):
        """
        Constructor de Torneo.
        :param nombre: Nombre del torneo.
        :param *equipos (tuple[Equipo]): Equipos participantes.
        """
        self._nombre = nombre
        self._equipos = list(equipos)

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
    def equipos(self)-> list[Equipo]:
        """
        Getter para equipos.
        """
        return self._equipos

    @equipos.setter
    def equipos(self, *equipos:tuple[Equipo])-> None:
        """
        Setter para equipos.
        """
        self._equipos = list(equipos)

    def agregar_equipos(self, *equipos:tuple[Equipo])-> None:
        """
        Añade uno o más equipos al torneo.
        :param equipos: Equipo u equipos a añadir.
        :return: No devuelve nada.
        """
        for equipo in equipos:
            if equipo not in self._equipos:
                self._equipos.append(equipo)
            else:
                print(f"{equipo.nombre}")

    def eliminar_equipo(self, *equipos):
        """
        Elimina uno o más equipos del torneo.
        :param equipos: Equipo u equipos a eliminar.
        :return: No devuelve nada.
        """
        for equipo in equipos:
            if equipo in self.equipos:
                self.equipos.remove(equipo)
                print(f"Equipo '{equipo.nombre}' eliminado del torneo.")
            else:
                print(f"Equipo '{equipo.nombre}' no está en el torneo.")

    def mostrar_equipos(self)-> None:
        """
        Muestra en pantalla la lista de equipos participantes en el torneo.
        :return: No devuelve nada.
        """
        print(f"Equipos: {self._nombre}:")
        for equipo in self._equipos:
            print(equipo)

    def generar_rol(self)-> None:
        """
        Genera y muestra el rol de enfrentamientos de todos contra todos en la jornada.
        Si hay menos de 2 equipos no se hace el rol y si el número de equipos es impar, genera un equipo extra.
        :return: No devuelve nada.
        """
        if len(self._equipos) < 2:
            print("Equipos insuficientes")
        else:
            if len(self._equipos) % 2 != 0:
                print("El número de equipos debe ser par, así que se agregará un extra.")
                self.agregar_equipos("Extra")
                print("Se agregó un equipo extra.")
            print("Creando rol...")
            mitad = len(self._equipos) // 2
            equipos_a = []
            equipos_b = []

            for i in range(len(self._equipos)):
                if i < mitad:
                    equipos_a.append(self._equipos[i])
                else:
                    equipos_b.append(self._equipos[i])

            for ronda in range(1, len(self._equipos) ):
                print(f"\nRonda {ronda}:")
                for i in range(mitad):
                    print(f"{equipos_a[i]} vs {equipos_b[i]}")

                if ronda < len(self._equipos)-1:
                    # Guardar el primer elemento de equipos_b
                    primer_b = equipos_b.pop(0)
                    # Insertarlo en la segunda posición de equipos_a
                    equipos_a.insert(1, primer_b)
                    # Mover el último de equipos_a al final de equipos_b
                    ultimo_a = equipos_a.pop()
                    equipos_b.append(ultimo_a)


    def __str__(self) -> str:
       equipos = ", ".join(str(equipo) for equipo in self._equipos)
       return f"Torneo(Nombre: {self._nombre}, equipos: ({equipos})"




""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    """
    Función principal para la clase Torneo.
    """