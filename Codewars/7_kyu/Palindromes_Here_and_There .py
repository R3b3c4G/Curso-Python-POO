"""
Nombre: Rebeca Gregorio Espina.
Fecha: 31 de marzo de 2025.
Descripción:
Se proporciona una matriz con números palíndromos y no palíndromos. Un número palíndromo es un número que es igual en orden inverso.
Por ejemplo, 122 no es un número palíndromo, pero 202 sí.
Su tarea es escribir una función que devuelva una matriz con solo 1's y 0's, donde todos los números palíndromos
se reemplazan con 1 y todos los números no palíndromos se reemplazan con 0.

Por ejemplo:
[101, 2, 85, 33, 14014] -> [1, 1, 0, 1, 0]
[45, 21, 303, 56] -> [0, 0, 1, 0]
"""
from random import randint

def convert_palindromes(numbers: list[int])-> list[int]:
    """
    Esta función convierte una lista de números en una lista de 1's y 0's; 1 si el
    número es palíndromo o 0 si no es palíndromo.
    :param numbers: Lista de números enteros a evaluar.
    :return: Lista de 1's y 0's dependiendo si cada número es palíndromo.
    """
    n_numbers = []  # Lista para 1's y 0's.
    for num in numbers:
        cadena_num = str(num)   # Convertir número de la lista a cadena.
        valor = 1   # Asumir inicialmente que es palíndromo.
        longitud = len(cadena_num)   # Comparar dígitos desde los extremos hacia el centro.
        for i in range(longitud // 2):
            if cadena_num[i] != cadena_num[longitud - 1 - i]:
                valor = 0
                break
        n_numbers.append(valor)
    return n_numbers

if __name__ == '__main__':
    """
    Función principal que genera un lista de números enteros,
    manda a evaluar si son palíndromos y finalmente imprime el resultado.
    """
    mi_arreglo = []
    cont = randint(1, 9)    # Valor aleatorio para el número de elementos para la lista.
    for a in range(cont):
        mi_arreglo.append(randint(0,5000))
    nuevo_arreglo = convert_palindromes(mi_arreglo)
    print(f"{mi_arreglo}\n\n{nuevo_arreglo}")