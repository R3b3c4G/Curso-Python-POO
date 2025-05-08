"""
Nombre: Rebeca Gregorio Espina.
Fecha: 9 de mayo del 2025.
Descripción:
Crear un algoritmo para contar el número de ceros que aparecen entre 1 y N.
Ejemplos
     10 --> 1 // 10
     20 --> 2 // 10, 20
    100 --> 11 // 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    200 --> 31
"""
from random import randint

def count_zeros(x:int) -> int:
    """
    Función para contar el número de ceros que aparecen entre 1 y N.
    :param x: Número entero a procesar.
    :return: Cantidad de ceros que aparecen entre 1 y N.
    """
    contador = 0
    for num in range(1, x + 1):   # Iterar sobre los elementos de x.
        for digito in str(num): # Revisar cada dígito.
            if digito == "0":
                contador += 1
    return contador

if __name__ == "__main__":
    """
    Función principal para probar la funcionalidad de la función  "count_zeros".
    """
    numero = randint(1, 5000)
    print(f"{numero} --> {count_zeros(numero)}")
