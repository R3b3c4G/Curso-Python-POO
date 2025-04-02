"""
Nombre: Rebeca Gregorio Espina.
Fecha: 18 de marzo de 2025
Descripción:
A Nathan le encanta el ciclismo.
Como Nathan sabe que es importante mantenerse hidratado, bebe 0,5 litros de agua por cada hora de ciclismo.
Te dan el tiempo en horas y debes devolver el número de litros que beberá Nathan, redondeado hacia abajo.
Por ejemplo:
    tiempo = 3 ----> litros = 1
    tiempo = 6.7---> litros = 3
    tiempo = 11.8--> litros = 5
"""
def litres(time:float)-> int:
    """
    Función para calcular el litro de agua a tomar.
    :param time: Tiempo en horas de ciclismo.
    :return: Regresa el litro de agua que debe consumir dependiendo del tiempo de ciclismo.
    """
    return int(time * 0.5)


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

if __name__ == "__main__":
    """
    Función principal.
    """
    cadena_tiempo = input("Ingresa el tiempo de ciclismo: ")
    tiempo = cadena_a_flotante(cadena_tiempo)
    while tiempo is None:
        print("Opción no válida, intenta nuevamente.")
        print()
        cadena_tiempo = input("Ingresa un número flotante: ")
        tiempo = cadena_a_flotante(cadena_tiempo)
    tomar_agua = litres(tiempo)
    print()
    print(f"Consume {tomar_agua} litros de agua.")
    print()
    print("Fin del programa.")