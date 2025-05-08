"""
Nombre: Rebeca Gregorio Espina.
Fecha: 18 de marzo de 2025
Descripción:
Mientras creaba un juego, tu compañero Greg decidió crear una función para comprobar si el usuario sigue vivo checkAlive/CheckAlive/check_alive.
Desafortunadamente, Greg cometió algunos errores al crear la función.
checkAlive debe devolver verdadero si la salud del jugador es mayor que 0 o falso si es 0 o menor.
La función recibe un parámetro health que siempre será un número entero entre -10 y 10.
"""
from random import randint


def check_alive(health:int)-> bool:
    """
    Función que determinar si un usuario está vivo basado en su salud.
    :param health: Salud del personaje.
    :return: Retorna un valor booleano; True si el usuario está vivo o False si está muerto.
    """
    if health <= 0:
        return False
    else:
        return True

if __name__ == "__main__":
    """
    Función principal.
    """
    health_u = randint(-10,10)    # Generar número entero aleatorio entre -10 y 10.
    print(health_u)
    print(check_alive(health_u))
