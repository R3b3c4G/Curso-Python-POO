"""
Nombre: Rebeca Gregorio Espina.
Fecha: 25 de junio del 2025.
Descripción:
Paso 1: Cree una función llamada encode()para reemplazar todas las vocales minúsculas en una cadena
dada con números de acuerdo con el siguiente patrón:
    a -> 1
    e -> 2
    i -> 3
    o -> 4
    u -> 5
Por ejemplo, encode("hello")devolvería "h2ll4". No hay necesidad de preocuparse por las vocales mayúsculas en este kata.

Paso 2: Ahora crea una función llamada decode()para convertir los números nuevamente en vocales de acuerdo
con el mismo patrón que se muestra arriba.

Por ejemplo, decode("h3 th2r2")devolvería "hi there".
Para simplificar, puedes asumir que cualquier número pasado a la función corresponderá a vocales.
"""
def encode(st):
    """
    Función que codifica todas las vocales minúsculas en una cadena
    dada con números de acuerdo con el siguiente patrón:
    a -> 1
    e -> 2
    i -> 3
    o -> 4
    u -> 5
    :param st: Cadena de texto a codificar.
    :return:Cadena con las vocales reemplazadas por sus respectivos valores numéricos.
    """
    diccionario = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    numero = ""
    for digito in st:
        if digito in diccionario:   # Si el carácter es una vocal, lo reemplazamos con el número correspondiente.
            numero += str(diccionario[digito])
        else:
            numero += digito    # Si no es vocal, se conserva el carácter.
    return numero


def decode(st):
    """
    Función que decodifica una cadena de texto convirtiendo los números enteros del 1 al 5 en vocales minúsculas
    según el siguiente patrón (inverso):
        1 -> a
        2 -> e
        3 -> i
        4 -> o
        5 -> u
    :param st: Cadena decodificada.
    :return: Cadena con los números convertidos nuevamente en vocales.
    """
    diccionario = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
    numero = ""
    for digito in st:
        if digito in diccionario:   #  Si el carácter es un número entero entre 1 y 5, lo convertimos al vocal correspondiente.
            numero += str(diccionario[digito])
        else:   # Si no es un número entero entre 1 y 5, se conserva el carácter.
            numero += digito
    return numero

if __name__ == "__main__":
    # Función principal para probar la encode() y decode().
    print(f"decode(): hello --> {encode("hello")}")
    print(f"encode(): h3 th2r2 --> {decode("h3 th2r2")}")

