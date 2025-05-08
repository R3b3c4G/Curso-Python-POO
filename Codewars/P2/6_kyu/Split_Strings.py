"""
Nombre: Rebeca Gregorio Espina.
Fecha: 9 de mayo del 2025.
Descripción:
Complete la solución para que divida la cadena en pares de dos carácteres. Si la cadena contiene un número impar de carácteres,
debe reemplazar el segundo carácter faltante del último par con un guion bajo ('_').

Ejemplos:
    * 'abc' => ['ab', 'c_']
    * 'abcdef' => ['ab', 'cd', 'ef']
"""

def solution(s:str) -> list[str]:
    """
    Función para dividir una cadena en pares de dos carácteres y si la cadena contiene un número impar de carácteres,
    reemplaza el segundo carácter faltante del último par con un guion bajo ('_').
    :param s: Cadena a dividir.
    :return: Una lista de pares de carácteres de la cadena.
    """
    nuevo_s = []    # Lista vacía para guardar el par de carácteres.
    contador = 0
    # si la cadena contiene un número impar de carácteres, se agrega '_' al final de la cadena.
    if len(s) % 2 != 0:
        s +='_'
    # Ciclo que recorre la cadena(avanza de par en par).
    while contador < len(s):
        par = s[contador] + s[contador + 1]
        nuevo_s.append(par)
        contador += 2
    return nuevo_s


if __name__ == "__main__":
    """
    Función principal que solicita una cadena y manda a dividir la cadena en pares de dos carácteres.
    Al final imprime la cadena en pares de dos carácteres.
    """
    cadena = input("Ingresa tu cadena: ")
    print(f"'{cadena}' --> {solution(cadena)}")
