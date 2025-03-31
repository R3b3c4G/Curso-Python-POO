"""
Nombre: Rebeca Gregorio Espina.
Fecha: 31 de marzo de 2025
Descripción:
Se supone que el método elimina los números pares de la lista y devuelve una lista que contiene los números impares.
Sin embargo, hay un error en el método que necesita ser resuelto.

def kata_13_december(lst):
    # Fix this code
    for i in range(len(lst)):
        if lst[i]%2==0:
            lst.remove(i)
    return lst
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

def kata_13_december(lst):
    """
    Función que recibe una lista de números y retorna una nueva lista de números impares.
    :param lst: Lista de números (entero o flotante/par o impar).
    :return: Lista de números impares pertenecientes a la lista original.
    """
    impar_lst = []
    for i in lst:
        if i % 2 != 0:  # Si nos es par, el número se agrega a la lista impar.
            impar_lst.append(i)
    return impar_lst

if __name__ == "__main__":
    """
    Función principal que pide una lista de 5 números, los valida y finalmente imprime cual de ellos es impar.
    """
    lst = []
    print("Ingresa tu lista de números")
    for i in range (5):
        cadena_lst = input(f"[{i+1}].- ")
        lst_num = cadena_a_flotante(cadena_lst)
        while lst_num is None:
            print("Opción no válida, intenta nuevamente.")
            cadena_lst = input("Ingresa tu lista de números: ")
            lst_num = cadena_a_flotante(cadena_lst)
        lst.append(lst_num)
    print(kata_13_december(lst))