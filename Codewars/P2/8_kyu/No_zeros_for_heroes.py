"""
Nombre: Rebeca Gregorio Espina.
Fecha: 9 de mayo del 2025.
Descripción:
Los números que terminan en cero son aburridos.
Puede que sean divertidos en tu mundo, pero no aquí.
Deshazte de ellos. Solo de los finales.
1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105
0 -> 0
"""
from random import randint

def no_boring_zeros(n):
    """
    Función que elimina los ceros finales de un número entero.
    :param n: Número entero a procesar.
    :return: Número entero sin ceros al final.
    """
    if n != 0:
        while n % 10 == 0:  # Mientras s sea divisible entre 10
            n //= 10    # s = División entera entre 10.
    return n

if __name__ == "__main__":
    """
    Función principal para probar la funcionalidad de la función  "no_boring_zeros".
    """
    numero = randint(-5000, 5000)
    print(f"{numero} --> {no_boring_zeros(numero)}")
