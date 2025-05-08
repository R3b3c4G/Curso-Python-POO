"""
Nombre: Rebeca Gregorio Espina.
Fecha: 9 de mayo del 2025.
Descripción:
Corrija este código para que acepte un argumento x, que devuelva "x es mayor que cero" si x es positivo (y distinto de cero);
en caso contrario, devuelva "x es igual o menor que cero". En ambos casos, reemplácelo x con el valor real de x.
def corrections(x,y,z
    elif x > 0
        append float(x) + (is more than zero."
    elsse
        retorn float(x) + "is equal to or less than zero.)
"""
from random import randint

def corrections(x):
    """
    Función para evaluar si un número entero es positivo y devuelve el mensaje "x es mayor que cero" si x es positivo (y distinto de cero),
    en caso contrario, devuelve "x es igual o menor que cero".
    :param x: Un número entero aleatorio.
    :return: "x es mayor que cero" si x es positivo (y distinto de cero), en caso contrario, devuelve "x es igual o menor que cero".
    """
    # Código corregido.
    # Faltaba punto y coma, paréntesis, algunas palabras reservadas estaban mal escritas.
    if x > 0:
        return  f"{x} is more than zero."
    return f"{x} is equal to or less than zero."

if __name__ == "__main__":
    """
    Función principal para probar la funcionalidad de la función  "corrections".
    """
    numero = randint(-50, 50)
    print(corrections(numero))
