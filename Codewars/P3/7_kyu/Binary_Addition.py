"""
Nombre: Rebeca Gregorio Espina.
Fecha: 12 de junio del 2025.
Descripción:
Descripción:
Implementa una función que suma dos números y devuelve su suma en binario. La conversión puede realizarse antes o después de la suma.
El número binario devuelto debe ser una cadena.

Ejemplos: (Entrada1, Entrada2 --> Salida (explicación))
    1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
    5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
"""
def add_binary(a,b):
    """
    Función que suma dos números enteros y los devuelve en formato binario.
    :param a: Primer número entero.
    :param b: Segundo número entero.
    :return: Cadena de binario que representa la suma de a + b.
    """
    # La función bin() convierte un número entero a su representación binaria, devolviendo una cadena comenzando con el prefijo "0b"
    resultado = bin(a + b)
    return resultado[2:]    # Se devuelve la cadena de binario, omitiendo los primeros dos prefijos.

if __name__ == "__main__":
    """ 
    Función principal, para probar la función add_binary().
    """
    print(f"{1}, {1} --> {add_binary(1, 1)}")
    print(f"{5}, {9} --> {add_binary(5, 9)}")