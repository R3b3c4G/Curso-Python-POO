"""
Nombre: Rebeca Gregorio Espina.
Fecha: 9 de mayo del 2025.
Descripción:
Completa la función que devuelve el día de la semana según el número de entrada:

    1 devoluciones "Sunday"
    2 devoluciones "Monday"
    3 devoluciones "Tuesday"
    4 devoluciones "Wednesday"
    5 devoluciones "Thursday"
    6 devoluciones "Friday"
    7 devoluciones "Saturday"
    De lo contrario regresa "Wrong, please enter a number between 1 and 7".
"""
def validar_entero(cadena_num: str) -> int|None:
    """
    Función para validar si una cadena es un entero positivo.
    :param cadena_num: Cadena a validar.
    :return: Si la cadena es numérico lo devuelve en tipo entero y si no, devuelve None.
    """
    if cadena_num.isnumeric():
        return int(cadena_num)
    return None

def whatday(num:int) -> int|str:
    """
    Función devuelve un día de la semana dependiendo del número entero del 1-7 ingresado
    en el teclado y si no corresponde a esos números imprime el mensaje
    "Wrong, please enter a number between 1 and 7".
    """
    dias = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
        }
    if num in dias:
        return dias[num]  # Devuelve el día correspondiente
    else:
        return "Wrong, please enter a number between 1 and 7"

if __name__ == "__main__":
    """
    Función principal 
    """
    cadena = input("Ingresa un número entero entre 1-7: ")
    num_entero = validar_entero(cadena)
    while num_entero is None:
            print("Opción no válida, intenta nuevamente.")
            cadena = input("Ingresa un número entero entre 1-7: ")
            num_entero = validar_entero(cadena)
    print(f"'{num_entero}' --> {whatday(num_entero)}")





