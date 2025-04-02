"""
Nombre: Rebeca Gregorio Espina.
Fecha: 31 de marzo de 2025.
Descripción:
Dada una matriz de números, devuelve una matriz, con cada miembro de la matriz de entrada redondeado al número más cercano, divisible por 5.
Por ejemplo, dada la siguiente matriz:
[34.5, 56.2, 11, 13]
Debería regresar
[35, 55, 10, 15]
Los redondeos deben realizarse como "en la vida real":22.5 -> 25
"""
import random
from random import randint

def round_to_five(arr:list[float])-> list[int]:
    """
    Función que redondea cada número de una lista al múltiplo de 5 más cercano.
    :param arr: Lista de números flotantes a redondear.
    :return: Lista de enteros redondeados al múltiplo de 5 más cercano.
    """
    arr_r = []  # Lista para redondeos.
    for num in arr:
        num_r = int((num + 2.5) // 5) * 5
        arr_r.append(num_r)
    return arr_r

if __name__ == '__main__':
    """
    Función principal que genera una lista de números flotantes, los manda a redondear y
    finalmente imprime una lista con los valores redondeados.
    """
    mi_arreglo = [] # Lista para números flotantes.
    cont = randint(1,9) # Valor aleatorio para el número de elementos para la lista de números flotantes.
    for a in range(cont):
        # La función random. uniform() devuelve un número flotante aleatorio.
        valor_flotante = round(random.uniform(1, 30), 1)    # Se redondea a un decimal.
        mi_arreglo.append(valor_flotante)
    nuevo_arreglo = round_to_five(mi_arreglo)
    print(f"{mi_arreglo}\n\n{nuevo_arreglo}")


