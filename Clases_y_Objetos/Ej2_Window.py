from Ej2_Scoreboard import Scoreboard

"""
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de marzo de 2025.
Descripción:
Se necesita desarrollar un sistema que permita gestionar y visualizar un scoreboard (puntuación) dentro de una ventana gráfica.
En este programa contamos con una clase Window que interactúa con la clase Scoreboard a través de una relación de agregación.

2.-Ventana:
Debe contener un scoreboard como parte de su interfaz.
Debe permitir actualizar el puntaje del scoreboard.
Debe ser capaz de redibujar el scoreboard cuando se actualice la puntuación.
"""
class Window:
    """
    Clase que representa una ventana gráfica con un marcador de puntuación.

    Atributos:
        _title: Título de la ventana (protegido).
        _width: Ancho de la ventana (protegido).
        _height: Alto de la ventana (protegido).
        _scoreboard: Instancia de Scoreboard asociada a la ventana (protegido).
    Métodos:
        __init__(): Constructor para inicializar la ventana con un scoreboard.
        Métodos de acceso: Permiten acceder y modificar los atributos.
        draw_scoreboard(): Llama al método draw del scoreboard para mostrarlo en la ventana.
        update_score(): Actualiza la puntuación del scoreboard y lo redibuja.
        __str__(): Devuelve una representación en cadena del objeto.
    """
    def __init__(self, text:str, width:int, height:int, scoreboard:Scoreboard=Scoreboard()):
        """
        :param text: Título de la ventana
        :param width: Ancho de la ventana
        :param height: Altura de la ventana
        :param scoreboard: Instancia de Scoreboard.
        """
        # scoreboard: Scoreboard = Scoreboard(): Variable, Clase, Objeto
        self._title = text
        self._width = width
        self._height = height
        self._scoreboard = scoreboard

    def draw_scoreboard(self)-> None:
        """
        Llama al método draw del scoreboard para Dibuja el marcador de puntuación en la ventana.
        :return: No devuelve nada.
        """
        self._scoreboard.draw() # Similar

    def update_score(self, points:int)-> None:
        """
        Actualiza la puntuación del scoreboard y lo redibuja.
        :param points: Nuevo valor de puntuación.
        :return: No devuelve nada.
        """
        self._scoreboard.points = points
        self.draw_scoreboard()  # Es equivalente a self._scoreboard.draw().

    # Método de acceso title
    @property
    def title(self)-> str:
        """
        Getter para title.
        """
        return self._title

    @title.setter
    def title(self, text: str)-> None:
        """
        Setter para title.
        """
        self._title = text

    # Método de acceso width
    @property
    def width(self)-> int:
        """
        Getter para width.
        """
        return self._width

    @width.setter
    def width(self, width:int)-> None:
        """
        Setter para width.
        """
        self._width = width

    # Método de acceso height
    @property
    def height(self)-> int:
        """
        Getter para height.
        """
        return self._height

    @height.setter
    def height(self, height:int)-> None:
        """
        Setter para height.
        """
        self._height = height

    # Método de acceso Scoreboard
    @property
    def scoreboard(self)-> Scoreboard:
        """
        Getter para scoreboard.
        """
        return self._scoreboard

    @scoreboard.setter
    def scoreboard(self, scoreboard:Scoreboard)-> None:
        """
        Setter para scoreboard.
        """
        self._scoreboard = scoreboard

    def __str__(self)-> str:    # Devuelve una representación en cadena del objeto.
        return f"Window(title={self._title}, width={self._width}, height={self._height}, scoreboard={self._scoreboard}"

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    """
    Función principal para la clase Window.
    """
    # Se crean objetos de la clase Window sin un objeto de la clase Scoreboard creado
    # y se prueban sus métodos.
    print("  -- Se crea un objeto de la clase Window sin un objeto de la clase Scoreboard.")

    buscaminas = Window("Buscaminas", 800, 900, Scoreboard(0, text_color= (0, 0, 0), font="Kimono", size=48 ))

    print("Se imprime el objeto:")
    print(f"Buscaminas = {buscaminas}")

    print()
    print("Método para dibujar el scoreboard:")
    buscaminas.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    buscaminas.update_score(1)


    # Se crean objetos de ambas clases y se prueban sus métodos.
    print()
    print("  -- Se crea otro objeto de la clase Window, pero ahora con un objeto de la clase Scoreboard.")

    marcador_solitario = Scoreboard(10,(40, 40, 40), "Arial", 40)
    solitario = Window("Solitario", 1_000, 1_000, marcador_solitario)

    print("Se imprimen los objetos:")
    print(f"marcador_solitario = {marcador_solitario}")
    print(f"Solitario = {solitario}")

    print()
    print("Método para dibujar el scoreboard:")
    solitario.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    solitario.update_score(11)


    # Se modifican los atributos mediante los métodos de acceso.
    print()
    print("  -- Se modifican los atributos mediante los métodos de acceso.")

    print("Se tiene la ventana buscaminas:")
    print(f"buscaminas = {buscaminas}")
    print("Se reemplaza el scoreboard utilizando el setter:")
    buscaminas.scoreboard = marcador_solitario
    print(f"buscaminas = {buscaminas}")


