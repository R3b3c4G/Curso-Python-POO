"""
Nombre: Rebeca Gregorio Espina.
Fecha: 9 de mayo del 2025.
Descripción:
Escriba una función que creará una cadena a partir de una lista de cadenas, separadas por espacios.
Ejemplo:
    ["hello", "world"] -> "hello world"
"""
def words_to_sentence(words):
    """
    Función para crear una cadena separada por espacios esto a partir de una lista.
    :param words: Lista de cadenas.
    :return: Una sola cadena separada por espacios.
    """
    cadena_lista = words[0]
    for i in range(len(words)):
        cadena_lista += " " + words[i]
    return cadena_lista

if __name__ == "__main__":
    """
    Función principal que solicita cadenas de texto, las guarda en una lista para mandar a
    crear una sola cadena separada por espacios.
    """
    arrays = []
    cadena = input("Ingresa tu cadena: ")
    while not cadena:
        cadena = input("Ingresa tu cadena: ")
    while cadena:
        arrays.append(cadena)
        cadena = input("Ingresa tu siguiente cadena o presione (ENTER) para salir: ")
    print(f"{arrays} --> {words_to_sentence(arrays)}")
