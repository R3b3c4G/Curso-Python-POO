"""
Nombre: Rebeca Gregorio Espina.
Fecha: 31 de marzo de 2025.
Descripción:
Reemplace todas las vocales por signos de exclamación en la oración. aeiouAEIOU es vocal.
Ejemplos:
    "Hi!" --> "H!!"
    "!Hi! Hi!" --> "!H!! H!!"
    "aeiou" --> "!!!!!"
    "ABCDE" --> "!BCD!"
"""
def replace_exclamation(st:str)-> str:
    """
    Función para remplazar las vocales de en una cadena por signos de exclamación.
    :param st: Cadena de texto a evaluar.
    :return: Devuelve una nueva cadena similar a la original excepto que todas las vocales
            que son reemplazadas por "!".
    """
    st2 = ""    # cadena para almacenar el resultado.
    for caracter in st:
        if caracter.lower() in "aeiou":
            st2 += "!"
        else:
            st2 += caracter
    return st2

if __name__ == "__main__":
    """
    Función principal que solicita una palabra u oración, lo manda a evaluar y
    finalmente imprime lo ingresado sin embargo remplazando las vocales con "!".
    """
    oracion = input("Ingresa una palabra u oración: ")
    print(oracion," --> ",replace_exclamation(oracion))