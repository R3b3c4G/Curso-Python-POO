"""
Nombre: Rebeca Gregorio Espina.
Fecha: 9 de mayo del 2025.
Descripción:
Escriba la función RemoveExclamationMarks que elimina todos los signos de exclamación de una cadena determinada.
"""
def remove_exclamation_marks(s:str)-> str:
    """
    Función para eliminar todos los signos de exclamación de una cadena determinada.
    :param s: Cadena
    :return: La cadena sin signos de exclamación.
    """
    # La función replace() remplaza las exclamaciones que tenga la cadena, por un vacío.
    s = s.replace("!", "")
    s = s.replace("¡", "")
    # Se regresa la misma cadena sin signos de exclamación.
    return s


if __name__ == "__main__":
    """
    Función principal que solicita una cadena y manda a eliminar los signos de
    exclamación que tenga.
    """
    cadena = input("Ingresa tu cadena: ")
    print(f"'{cadena}' --> {remove_exclamation_marks(cadena)}")
