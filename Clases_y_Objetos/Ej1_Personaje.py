"""
Nombre: Rebeca Gregorio Espina.
Fecha: 12 de marzo de 2025
Descripción:
Crea una clase llamada Personaje que simule los movimientos de un personaje de videojuegos en una ventana.
1. El personaje se moverá por una ventana de tamaño máximo (x, y) = (10, 10) y podrá realizar los siguientes movimientos si no supera el límite de la ventaja:
      * Avanzar (caracteres 'A' o 'a'): aumenta en 1 la posición en y,
      * Retroceder (caracteres 'R' o 'r'): disminuye en 1 la posición en y,
      * Derecha (caracteres 'D' o 'd'): aumenta en 1 la posición en x,
      * Izquierda (caracteres 'I' o 'i'): disminuye en 1 la posición en x.

2. El personaje tendrá los siguientes métodos (además de los métodos mágicos):
      * moverse() que recibe la orden como parámetro,
      * posicion_actual() que muestra en consola la posición en (x,y).
3. Se debe llevar un registro del ID de los personajes creados, por lo que se debe utilizar un atributo de clase.
4. Al crear los objetos de la clase, inicialmente deben establecerse en el origen (x, y) = (0, 0).
5. Se debe solicitar iterativamente la secuencia de movimientos e indicar la posición final de la secuencia.
6. El programa se detendrá con los caracteres 'S' o 's'.
"""
class Personaje:
    """
    Clase que representa a un personaje.
    Sus atributos son: id (atributo de clase), x,y (coordenadas).
    Sus métodos son: __init__(), __str__(), moverse() y posicion_actual().
    """
    id = 1
    def __init__(self):
        """
        Constructor de la clase personaje.
        Asigna una posición inicial en (0,0) y un ID por cada personaje.
        """
        # Inicializar coordenada.
        self.x = 0
        self.y = 0
        self.id_personaje = Personaje.id
        Personaje.id += 1

    def moverse(self, ordenes:str)-> None:

        """
        Se utiliza para mover al personaje de acuerdo al caracter ingresado.
        :param ordenes: Caracter ingresado (movimiento correspondiente).
        """
        """
        * Avanzar (caracteres 'A' o 'a'): aumenta en 1 la posición en y,
        * Retroceder (caracteres 'R' o 'r'): disminuye en 1 la posición en y,
        * Derecha (caracteres 'D' o 'd'): aumenta en 1 la posición en x,
        * Izquierda (caracteres 'I' o 'i'): disminuye en 1 la posición en x.
        """
        for caracter in ordenes:
            if caracter == 'a' and self.y < 11:
                self.y += 1
            if caracter == 'r' and self.y > 0:
                self.y -= 1
            if caracter == 'd' and self.x < 11:
                self.x += 1
            if caracter == 'i' and self.x > 0:
                self.x -= 1

    def posicion_actual(self)-> None:
        print(f"Posición actual: (x, y) = ({self.x}, {self.y})")

    def __str__(self) -> str:
        """
        Se utiliza para definir la representación en cadena del personaje.
        :return: El objeto en forma de cadena.
        """
        return f"Posición actual: (x, y) =  ({self.x},  {self.y}))"

if __name__=="__main__":
    "Función principal."
    sonic = Personaje() # Crea una instancia del personaje.
    mis_ordenes = None
    while mis_ordenes!= "s" and mis_ordenes!= "S":
        mis_ordenes = input("Ingresa las coordenadas de movimiento:  ").lower()
        sonic.moverse(mis_ordenes)
        sonic.posicion_actual()
    print("Fin del programa.")