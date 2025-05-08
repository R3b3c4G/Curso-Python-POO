"""
Nombre: Rebeca Gregorio Espina.
Fecha: 9 de mayo del 2025.
Descripción:
La raíz digital es la suma recursiva de todos los dígitos de un número.
Dado n, se calcula la suma de los dígitos de n. Si ese valor tiene más de un dígito, se continúa
reduciendo de esta manera hasta obtener un número de un solo dígito. La entrada será un entero no negativo.
Ejemplos
    16 --> 1 + 6 = 7
    942 --> 9 + 4 + 2 = 15 --> 1 + 5 = 6
    132189 --> 1 + 3 + 2 + 1 + 8 + 9 = 24 --> 2 + 4 = 6
    493193 --> 4 + 9 + 3 + 1 + 9 + 3 = 29 --> 2 + 9 = 11 --> 1 + 1 = 2
"""
def validar(v_numero:str) -> int|None:
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

def digital_root(n:int) -> int:
    """
    Función para calcular la raíz dígital, donde se suman los dígitos del número y se repite el proceso con el
    resultado hasta obtener un único dígito.
    :param n: Número entero positivo a procesar.
    :return: Un entero positivo de un dígito.
    """
    while len(str(n)) != 1: # Mientras tenga más de un dígito.
        suma = 0    # Se reinicia la suma en cada iteración.
        for i in str(n): # Convertir n a cadena para iterar sobre cada dígito.
            suma += int(i)  # Convertir cada dígito a entero.
        n = suma
    return n

if __name__ == '__main__':
    """
    Función principal que solicita un número entero positivo a, lo manda a validar, calcula y muestra la 
    raíz dígital del número entero positivo ingresado.
    """
    c_numero = input("Ingresa un número positivo: ")
    numero = validar(c_numero)
    while numero is None:
        c_numero = input("Intenta nuevamente, ingresa un número positivo: ")
        numero = validar(c_numero)
    print(f"{numero} --> {digital_root(numero)}")
