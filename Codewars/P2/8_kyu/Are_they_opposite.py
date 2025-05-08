"""
Nombre: Rebeca Gregorio Espina.
Fecha: 9 de mayo del 2025.
Descripción:
Proporciona dos cadenas: s1 y s2. Si son opuestas, devuelve true; de lo contrario, devuelve false.
Nota: El resultado debe ser un valor booleano, no una cadena.
El opposite significado: Todas las letras de las dos cadenas son iguales, pero el caso es el opuesto. Se puede
asumir que la cadena solo contiene letras o que está vacía. También tenga
en cuenta el caso extremo: si ambas cadenas están vacías, se debe devolver false/ False.

Ejemplos (entrada -> salida)
    "ab","AB" -> true
    "aB","Ab" -> true
    "aBcd","AbCD" -> true
    "AB","Ab" -> false
    "","" -> false
"""
def is_opposite(s1:str,s2:str) -> bool:
    """
    Función que determina si dos cadenas son opuestas.
    :param s1: Primera cadena.
    :param s2: Segunda cadena.
    :return: true si son opuestos o false si no son opuestos.
    """
    # False: Si longitud de las cadenas no coincide o si están vacías.
    if len(s1) != len(s2) or not s1 and not s2:
        return False
    for caracter in range(len(s1)):
        # False: Si las el carácter de las cadenas originales son iguales.
            # False: Si no aplica en caso anterior, se verifica que los carácteres de la cadena en minúscula no sean iguales.
        if s1[caracter] == s2[caracter] or s1[caracter].lower() != s2[caracter].lower():
            return False
    # Si no cumplieron con los casos específicados, las cadenas son opuestos.
    return True

if __name__ == "__main__":
    """
    Función principal que solicita dos cadenas, lo manda a evaluar y
    finalmente imprime el resultado de si son opuestos.
    """
    cadena1 = input("Ingresa tu cadena 1: ")
    cadena2 = input("Ingresa tu cadena 2: ")
    print(f"'{cadena1}','{cadena2}' --> {is_opposite(cadena1, cadena2)}")
