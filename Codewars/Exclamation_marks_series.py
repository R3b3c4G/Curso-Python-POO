"""
Nombre: Rebeca Gregorio Espina.
Fecha: 31 de marzo de 2025
Descripción:
Reemplace todas las vocales por signos de exclamación en la oración. aeiouAEIOU es vocal.
Ejemplos:
    "Hi!" --> "H!!"
    "!Hi! Hi!" --> "!H!! H!!"
    "aeiou" --> "!!!!!"
    "ABCDE" --> "!BCD!"
"""
def replace_exclamation(st)-> str:
    st2 = ""
    for caracter in st:
        if caracter.lower() in "aeiou":
            st2 += "!"
        else:
            st2 += caracter
    return st2

if __name__ == "__main__":
    oracion = input("Ingresa una palabra u oración: ")
    print(oracion," --> ",replace_exclamation(oracion))