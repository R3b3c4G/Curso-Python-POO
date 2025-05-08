"""
Nombre: Rebeca Gregorio Espina.
Fecha: 9 de mayo del 2025.
Descripción:
Dada un vector de números enteros, devuelve una nueva matriz con cada valor duplicado.
Por ejemplo:
    [1, 2, 3] --> [2, 4, 6]
"""
from random import randint

def maps(a:list[int]) -> list[int]:
    """
    Función para duplicar los valores de una matriz.
    :param a: Lista de números a duplicar.
    :return: Una nueva lista con cada elemento duplicado.
    """
    nuevo_a = []
    for num in a:
        nuevo_a.append(num * 2)
    return nuevo_a

if __name__ == "__main__":
    """
    Función principal, determina la cantidad de elementos de la lista, los elementos de la lista
    y los manda a duplicar cada elemento de la lista.
    """
    vector = []
    contador = randint(2,15)    # Longitud aleatoria de la lista (2-15 elementos).
    for i in range(contador):
        numero = randint(-500,500) # Números aleatorios (-500 a 500) para los elementos de la lista.
        vector.append(numero)
    print(f"'{vector}' --> {maps(vector)}")


