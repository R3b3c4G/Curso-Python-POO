"""
Nombre: Rebeca Gregorio Espina.
Fecha: 31 de marzo de 2025.
Descripción:
Escriba una función que acepte un entero s no negativo y una cadena n como parámetros,
y devuelva una cadena s repetida exactamente n veces.

Ejemplos (entrada -> salida)
6, "I" -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
"""

def repeat_str(repeat:int, string:str)-> str:
    """
    Función para repetir una cadena en un número de veces indicado.
    :param repeat: Número de repeticiones.
    :param string: Cadena a repetir.
    :return: Devuelve la cadena resultante de repetir el texto.
    """
    n_string = ""
    for a in range(repeat):
        n_string += string
    return n_string

def validar(v_numero:str)-> int|None:
    """
    Función que valida y convierte una cadena a entero positivo.
    :param v_numero: Cadena a validar.
    :return: Devuelve el entero convertido si es válido, None si no cumple con los requisitos.
    """
    if v_numero.isdigit():
        if int(v_numero) >= 0:
            return int(v_numero)
        else:
            return None


if __name__ == '__main__':
    """
    Función principal que solicita un número entero positivo a, lo manda a validar, pide una frase b y
    finalmente imprime una cadena de la frase repetida a veces.
    """
    c_numero = input("Ingresa un número positivo: ")
    numero = validar(c_numero)
    while numero is None:
        print("Intenta nuevamente.")
        c_numero = input("Ingresa un número positivo: ")
        numero = validar(c_numero)
    cadena = input("Ingresa tu frase: ")
    print(numero,", ",cadena," -> ",repeat_str(numero,cadena))