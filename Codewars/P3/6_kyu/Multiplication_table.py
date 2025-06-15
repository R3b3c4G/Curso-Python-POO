"""
Nombre: Rebeca Gregorio Espina.
Fecha: 12 de junio del 2025.
Descripción:
Su tarea es crear una tabla de multiplicar N×N, del tamaño proporcionado en el parámetro.
Por ejemplo, cuando se da size = 3:
    1 2 3
    2 4 6
    3 6 9
    Para el ejemplo dado, el valor de retorno debería ser:
    [[1,2,3],[2,4,6],[3,6,9]]
"""
def multiplication_table(size):
    """
    Función que genera una tabla de multiplicar N×N, donde cada fila x contiene los múltiplos del número x desde 1 hasta N.
    :param size: Número entero positivo que representa el tamaño de la tabla.
    :return: Lista de listas representando la tabla de multiplicar.
    """
    resultado = []
    for b in range(1, size+1):
        aux = []    # Auxiliar para guardar la lista de cada fila
        for a in range(1, size+1):
            aux.append(a*b) # Se multiplica cada columna (a) por la fila actual (b).
        resultado.append(aux)   # Se agrega la fila completa a la lista final.
    return resultado

if __name__ == "__main__":
    """ 
    Función principal, para probar la función multiplication_table().
    """
    ejemplos = [3, 5]    # Tamaños de tabla.
    for ejemplo in ejemplos:
        print(f"{ejemplo} --> {multiplication_table(ejemplo)}")
