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
def string_clean(s)-> str:
    s2 = ""
    """
    Function will return the cleaned string
    """
    for caracter in s:
        if not caracter in "0123456789":
            s2 += caracter
    return s2

if __name__ == "__main__":
    palabra = input("Capturar palabra: ")
    print(palabra," --> ",string_clean(palabra))