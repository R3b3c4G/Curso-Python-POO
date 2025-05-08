"""
Nombre: Rebeca Gregorio Espina.
Fecha: 9 de mayo del 2025.
Descripción:
Crea una función que tome un número entero como argumento y retorne "Even" para números pares
u "Odd" para números impares.
"""

def cadena_a_entero(cadena: str) -> int|None:
    """
    Función para convertir una cadena a entero, si cumple con el formato.
    :param cadena: Cadena a válidar.
    :return: Un entero si el número convertido a entero es válido o None si no representa un entero válido.
    """
    # Contar la cantidad de guiones en la cadena.
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip('-')
    if revisar_cadena.isnumeric() and no_guiones in (0, 1):
        return int(cadena)
    else:
        return None

def even_or_odd(number: int) -> str:
    """
    Función para determinar si un número entero es par o impar.
    :param number: Número entero a evaluar.
    :return: Devuelve "Even" para números pares y "Odd" para números impares.
    """
    if number % 2 == 0:
        return 'Even'
    return 'Odd'

if __name__ == "__main__":
    """
    Función principal que solicita un número entero, manda a validar y
    manda a determinar si es par o impar.
    """
    mi_cadena = input("Ingresa un número entero: ")
    numero = cadena_a_entero(mi_cadena)
    while numero is None:
        mi_cadena = input("Intenta nuevamente, ingresa un número entero: ")
        numero = cadena_a_entero(mi_cadena)
    print(f"'{mi_cadena}' --> {even_or_odd(numero)}")