"""
Nombre: Rebeca Gregorio Espina.
Fecha: 31 de marzo de 2025
Descripción:
Tu jefe decidió ahorrar dinero comprando un software de reconocimiento óptico de caracteres (OCC) de bajo precio para escanear el texto de
novelas antiguas en tu base de datos. Al principio, parece capturar las palabras correctamente, pero enseguida te das cuenta de que
introduce muchos números en lugares aleatorios del texto.

Ejemplos (entrada -> salida):
'! !' -> '! !'
'123456789' -> ''
'This looks5 grea8t!' -> 'This looks great!'
Tus compañeros, agobiados, te piden una solución para eliminar todos los números de este texto ilegible. Tu programa tomará una cadena,
eliminará todos los caracteres numéricos y devolverá una cadena con los espacios y caracteres especiales ~#$%^&!@*():;"'.,? intactos.
"""
def string_clean(s:str)-> str:
    """
    Función que elimina todos los caracteres numéricos de una cadena.
    :param s: Texto de entrada que mezclado con números.
    :return: Devuelve una cadena sin números(1-9).
    """
    s2 = ""
    for caracter in s:
        if not caracter in "0123456789":
            s2 += caracter
    return s2

if __name__ == "__main__":
    """
    Función que solicita una palabra, manda a quitar números y 
    finalmente imprime una cadena limpia.
    """
    palabra = input("Capturar palabra: ")
    print(palabra," --> ",string_clean(palabra))