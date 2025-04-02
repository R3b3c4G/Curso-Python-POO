"""
Nombre: Rebeca Gregorio Espina.
Fecha: 31 de marzo de 2025
Descripción:
Vas a preparar tostadas de una forma rápida y crees que deberías preparar varias tostadas a la vez. Así que intentas hacer seis tostadas.
Olvidaste contar el número de tostadas que pusiste allí, no sabes si pusiste exactamente seis rebanadas de tostadas en las tostadoras.
Define una función que cuente cuántas tostadas más (o menos) necesitas en las tostadoras. Aunque necesites más o menos, el número seguirá siendo positivo, no negativo.

Ejemplos:
Debes devolver la cantidad de tostadas que necesitas para meter (o sacar). Si son 5 aún puedes meter 1 tostada:
5 --> 1
Y por son 12 necesitas 6 tostadas menos (pero no -6):
12 --> 6
"""
def six_toast(num:int)-> int:
    """
    Función que calcula la diferencia entre el número de tostadas y el 6.
    :param num: Número de tostadas ingresadas.
    :return: Devuelve la diferencia con respecto a 6.
    """
    if num < 6:
        return 6 - num
    elif num > 6:
        return num - 6
    else:
        return 0

if __name__ == "__main__":
    """
    Función principal que permite ingresar tostadas, evalúa la diferencia y finalmente
    imprime el resultado.
    """
    space = input(" Presione espacio para ingresar tostadas y ENTER para finalizar: ")
    cont = 0
    for i in space:
        if i == " ":
            cont += 1
    print(cont," --> ",six_toast(cont))


