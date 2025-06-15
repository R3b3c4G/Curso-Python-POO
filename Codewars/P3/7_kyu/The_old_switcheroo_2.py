"""
Nombre: Rebeca Gregorio Espina.
Fecha: 12 de junio del 2025.
Descripción:
Esta es una continuación de mi kata, el antiguo switcheroo.
Escriba una función que tome una cadena y reemplace todas las letras con sus respectivas posiciones en el alfabeto inglés;
por ejemplo , 'a' is 1, 'z' is 26. La función no debe distinguir entre mayúsculas y minúsculas.
    'abc' --> '123'
    'ABC' --> '123'
    'codewars' --> '315452311819'
    'abc-#@5' --> '123-#@5'
"""
def encode(st):
    """
    Función que toma una cadena y reemplaza todas las letras con sus respectivas posiciones en
    el alfabeto inglés(a=1, b=2, ..., z=26), sin distinguir entre mayúsculas y minúsculas.
    :param st: Cadena a convertir.
    :return: Cadena del remplazo de st por su valor numérico en el alfabeto inglés.
    """
    # Diccionario del alfabeto (valor y posición).
    diccionario = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
    'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16,
    'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
    'y': 25, 'z': 26
    }
    numero = ""
    for digito in st.lower():
        # Se convierte la cadena en minúsculas para comparar con el diccionario.
        if digito in diccionario:
            # Si el carácter es igual a uno de los valores que están en el diccionario, se remplaza por el valor de la posición correspondiente.
            numero += str(diccionario[digito])
        else:
            # Si no, se conserva el carácter original.
            numero += digito
    return numero

if __name__ == "__main__":
    """ 
    Función principal, para probar la función encode().
    """
    ejemplos = ['abc', 'ABC', 'codewars', 'abc-#@5']
    for cadena in ejemplos:
        print(f"{cadena} --> {encode(cadena)}")