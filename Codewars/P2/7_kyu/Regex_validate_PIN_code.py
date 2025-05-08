"""
Nombre: Rebeca Gregorio Espina.
Fecha: 9 de mayo del 2025.
Descripción:
Los cajeros automáticos permiten códigos PIN de 4 o 6 dígitos, y los códigos PIN no pueden contener nada más
que exactamente 4 o exactamente 6 dígitos.
Si se pasa a la función una cadena PIN válidos, devuelve true, de lo contrario devuelve false.

Ejemplos (Entrada --> Salida)
    "1234" --> true
    "12345" --> false
    "a234" --> false
"""

def validate_pin(pin:str) -> bool:
    """
    Función para validar un PIN, que solamente debe tener 4 o 6 dígitos numéricos.
    :param pin: PIN a validar.
    :return: Devuelve True si el PIN es válido o False en caso contrario.
    """
    if pin.isnumeric():
        if len(pin)== 4 or len(pin)==6:
            return True
    return False

if __name__ == "__main__":
    """
    Función principal, solicita el PIN y manda a válidar
    """
    cadena = input("Ingresa tu PIN: ")
    print(f"'{cadena}' --> {validate_pin(cadena)}")

