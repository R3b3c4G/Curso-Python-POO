"""
Crea una función que acepte un número arbitrario de arrays y devuelva un único array generado añadiendo elementos de los argumentos pasados. Si uno de ellos es más corto que los demás, el resultado debe rellenarse con elementos vacíos.

Ejemplos:

interleave([1, 2, 3], ["c", "d", "e"]) == [1, "c", 2, "d", 3, "e"]
interleave([1, 2, 3], [4, 5]) == [1, 4, 2, 5, 3, None]
interleave([1, 2, 3], [4, 5, 6], [7, 8, 9]) == [1, 4, 7, 2, 5, 8, 3, 6, 9]
interleave([]) == []
"""
def interleave(*args:list[list]) -> list[str|None]:
    """
    Función para intercalar elementos de listas.
    Si una de las listas es más corta, se agrega None para a completar.
    :param args: Lista de listas de carácteres ingresados por el usuario.
    :return: Lista de carácteres intercalados de las listas.
    """
    intercalado = []    # Lista para guardar los elementos intercalados
    mayor = 0
    # Se busca la lista mas larga.
    for array in args:
        if len(array) > mayor:
            mayor = len(array)

    # Se intercalan los elementos.
    for i in range(mayor):
        for array in args:
            if i < len(array):
                intercalado.append(array[i])
            else:
                intercalado.append(None)
    return intercalado

if __name__ == "__main__":
    """
    Función principal que solicita una cadena, los guarda como lista y las intercala.
    """
    arrays = []
    cadena = input("Ingresa tu cadena o presione (ENTER) para salir: ").strip()
    while cadena:
        arrays.append(list(cadena)) # La cadena se guarda como lista.
        cadena = input("Ingresa tu siguiente cadena o presione (ENTER) para salir: ")
    print(f"({arrays}) --> {interleave(*arrays)}")