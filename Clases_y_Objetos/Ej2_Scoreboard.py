"""
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de marzo de 2025.
Descripción:
Se necesita desarrollar un sistema que permita gestionar y visualizar un scoreboard (puntuación) dentro de una ventana gráfica.
En este programa contamos con una clase Scoreboard.

1. Scoreboard:
Debe almacenar y gestionar la puntuación actual,
Debe permitir actualizar la posición,
Debe ser capaz de dibujarse en pantalla con un formato específico.

La lógica del scoreboard está encapsulada en una clase independiente.
"""

class Scoreboard:
    """
    Clase que representa un marcador de puntuación.
    Atributos:
        _points: Almacena la puntuación actual (protegido).
        _text_color: Define el color del texto del scoreboard (protegido).
        _font: Especifica la fuente del texto (protegido).
        _size: Define el tamaño del texto (protegido).

        Métodos:
            __init__(): Constructor para inicializar el scoreboard.
            Métodos de acceso: Permiten acceder y modificar los atributos.
            draw(): Dibuja el scoreboard en la pantalla.
            __str__(): Devuelve una representación en cadena del objeto.
    """
    def __init__(self, points:int=0, text_color:tuple[int,int,int]=(0,0,0), font:str="kimono", size:float=48):
        """
        :param points: Puntuación inicial teniendo por default 0.
        :param text_color:  Color RGB del texto teniendo por default (0,0,0).
        :param font: Nombre de la fuente teniendo por default "kimono".
        :param size: Tamaño de la fuente teniendo por default 48.
        """
        self._points = points
        self._text_color = text_color
        self._font = font
        self._size = size

    def draw(self) -> None:
        """
        Dibuja el scoreboard en la pantalla.
        :return: No devuelve nada.
        """
        print(f"Score = {self.points}")
    # A continuación se hace el encapsulamiento de atributos que serán protegidos.
    # Se utiliza @property para indicar que es un getter del atributo protegido.
    # Se utiliza @nombre_de_atributo. Setter para indicar que es un setter del atributo protegido.
    # Los métodos getter y setter nos permiten acceder y modificar los atributos de datos manteniendo la encapsulación.

    # Método de acceso points
    @property
    def points(self) -> int:
        """
        Getter para points.
        """
        return self._points

    @points.setter
    def points(self, points:int=0)-> None:
        """
        Setter para points.
        """
        self._points = points

    # Método de acceso text_color
    @property
    def text_color(self)-> tuple[int,int,int]:
        """
        Getter para text_color.
        """
        return self._text_color

    @text_color.setter
    def text_color(self, text_color:tuple[int,int,int]) -> None:
        """
        Setter para text_color.
        """
        self._text_color = text_color

    # Método de acceso font
    @property
    def font(self) -> str:
        """
        Getter para font.
        """
        return self._font

    @font.setter
    def font(self, font:str)-> None:
        """
        Setter para font.
        """
        self._font = font

    # Método de acceso size
    @property
    def size(self)-> float:
        """
        Getter para size.
        """
        return self._size

    @size.setter
    def size(self, size:float)-> None:
        """
        Setter para size.
        """
        self._size = size

    def __str__(self)-> str:    # Devuelve una representación en cadena del objeto.
        return f"Scoreboard(points={self._points}, text_color={self._text_color}, font={self._font}, size={self._size})"

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    """
    Función principal para la clase Scoreboard.
    """
    # Se crean objetos de la clase y se imprime.
    print("  -- Se crean objetos de la clase Scoreboard.")
    print()
    print("Se crea un objeto sin argumentos:")
    marcador1 = Scoreboard()
    print(f"marcador1 = {marcador1}")

    print()
    print("Se crea otro objeto con (points, font y text_color) como argumentos por nombre:")
    marcador2 = Scoreboard(10, font="Arial", text_color= (127, 127, 127))
    print(f"marcador2 = {marcador2}")

    print()
    print("Se prueba el método draw() en ambos objetos:")
    marcador1.draw()
    marcador2.draw()