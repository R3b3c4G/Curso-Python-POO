"""
Nombre: Rebeca Gregorio Espina.
Fecha: 18 de marzo de 2025
Descripción:
Necesitamos una función simple que determine si se requiere un plural. Debería tomar un número y devolver "true" si se debe usar un plural con ese número, o "false" si no. Esto sería útil al imprimir una cadena como 5 minutes, 14 apples o 1 sun.
Solo tienes que preocuparte por las reglas gramaticales inglesas para este kata, donde cualquier cosa que no sea singular (uno de algo), es plural (no uno de algo).

Todos los valores serán números enteros positivos, flotantes o cero.
"""
def cadena_a_flotante(cadena:str)-> float|None:
    """
    Función que convierte una cadena de texto a un número flotante.
    :param cadena: Cadena de texto que se desea validar y convertir a flotante.
    :return: Retorna el número flotante si la cadena es válida o None si la cadena no cumple con el formato.
    """
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena =cadena.lstrip('-').replace(".","")
    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None

def plural(n:float)-> bool:
    """
    Función que determina si un número debería considerarse plural.
    :param n: Número a evaluar.
    :return: Devuelve True si el número es plural, False si es singular.
    """
    if n != 1:
        return True
    else:
        return False

if __name__ == "__main__":
    """
    Función principal.
    """
    cadena_cantidad = input("Ingresa un número positivo: ")
    cantidad = cadena_a_flotante(cadena_cantidad)
    while cantidad is None or cantidad < 0:
        print("Opción no válida, intenta nuevamente.")
        cadena_cantidad = input("Ingresa un número positivo: ")
        cantidad = cadena_a_flotante(cadena_cantidad)
    print(plural(cantidad))