"""
Nombre: Rebeca Gregorio Espina.
Fecha: 12 de junio del 2025.
Descripción:
Escriba un método (o función, según el lenguaje) que convierta una cadena a camelCase, es decir,
todas las palabras deben tener su primera letra en mayúscula y se deben eliminar los espacios.

Ejemplos (entrada --> salida):
"hello case" --> "HelloCase"
"camel case word" --> "CamelCaseWord"
"""
def camel_case(s):
    """
    Función que convierte en mayúscula la primera letra de una palabra de una cadena y elimina los espacios.
    :param s: Cadena a convertir.
    :return: Cadena en formato CamelCase.
    """
    # .title() convierte el primer carácter de cada palabra en mayúscula y el resto en minúscula.
    # Después, .replace remplaza el espacio " " por un vacío "".
    return s.title().replace(" ", "")

if __name__ == "__main__":
    """ 
    Función principal, para probar la función camel_case().
    """
    ejemplos = ["hello case", "camel case word"]
    for ejemplo in ejemplos:
        print(f"{ejemplo} --> {camel_case(ejemplo)}")



