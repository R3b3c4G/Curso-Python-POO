"""
Nombre: Rebeca Gregorio Espina.
Fecha: 9 de mayo del 2025.
Descripción:
Escriba una función que devuelva una secuencia (el índice empieza por 1) de todos los caracteres pares de una
cadena. Si la cadena tiene menos de dos caracteres o más de 100, la función debe devolver "cadena no válida".
Por ejemplo:
    "abcdefghijklm" --> ["b", "d", "f", "h", "j", "l"]
    "a" --> "invalid string"
"""
def even_chars(st:str) -> str | list[int]:
    """
     Función obtiene todos los carácteres pares de una cadena. Si la cadena tiene menos de dos caracteres o más de 100,
     la función debe devolver "invalid string".
    :param st: Cadena principal.
    :return: Lista de carácteres pares de la cadena principal.
    """
    mi_lista = []
    # Si la cadena tiene menos de dos carácteres o más de 100.
    if len(st) < 2 or len(st) > 100:
        return "invalid string"

    for i in range(len(st)):
        if i % 2 != 0:  # Si los índices son impares.
            mi_lista.append(st[i])
    return mi_lista

if __name__ == "__main__":
    """
    Función principal que solicita una cadena y consigue la lista de carácteres pares de la cadena proporcionada.
    """
    cadena = input("Ingresa tu cadena: ")
    print(f"{cadena} --> {even_chars(cadena)}")