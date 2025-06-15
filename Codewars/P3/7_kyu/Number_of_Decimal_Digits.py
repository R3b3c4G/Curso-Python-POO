"""
Nombre: Rebeca Gregorio Espina.
Fecha: 12 de junio del 2025.
Descripción:
Determine el número total de dígitos del entero (n>=0) dado como entrada a la función. Por ejemplo, 9 tiene un solo dígito,
66 tiene 2 dígitos y 128685 tiene 6 dígitos. Tenga cuidado para evitar desbordamientos o sub-desbordamientos.
Todas las entradas serán válidas.
"""

def digits(n):
    """
    Función que determina el número total de dígitos un entero mayor o igual a cero.
    :param n: Número entero mayor o igual a cero.
    :return: Número de dígitos del entero.
    """
    if n >= 0:
        # n se convierte en una cadena y se se retorna su longitud (número de dígitos).
        return len(str(n))

if __name__ == "__main__":
    """ 
    Función principal, para probar la función digits().
    """
    ejemplos = [9, 66, 128685]
    for numero in ejemplos:
        print(f"{numero} --> {digits(numero)}")