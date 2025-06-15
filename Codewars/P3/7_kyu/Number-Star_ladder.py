"""
Nombre: Rebeca Gregorio Espina.
Fecha: 12 de junio del 2025.
Descripción:
Descripción:
Usando n como parámetro en la función pattern, donde n > 0, completa el código para obtener el patrón:
    1
    1*2
    1**3
    1***4
    ... and so on...
Nota: No hay nueva línea al final (después de que termina el patrón).

Ejemplos
pattern(3): Debería devolver "1\n1*2\n1**3", por ejemplo, lo siguiente:
    1
    1*2
    1**3

pattern(10):Debería devolver lo siguiente:
    1
    1*2
    1**3
    1***4
    1****5
    1*****6
    1******7
    1*******8
    1********9
    1*********10
"""
def pattern(n):
    """
    Función que genera un patrón de texto en el que cada línea comienza con '1' seguida de
    asteriscos, así como en el siguiente ejemplo donde n = 3:
    1
    1*2
    1**3
    Los asteriscos se empiezan a incluir, si n > 1.
    :param n: Un número entero mayor a 0.
    :return: Cadena con el patrón generado, sin salto de línea final.
    """
    cadena = "1"    # n > 0, por lo tanto, '1' es un valor fijo del patrón.
    for a in range(1, n): # Si n > 1 se agrega un salto de línea antes de crear el siguiente patrón.
        # En cada iteración, se crea el patrón de cada fila; se agrega "1" al inicio de la línea,
        # seguido de número de asteriscos igual al índice actual (a), seguido del número (a + 1) como texto.
        cadena += "\n"
        cadena += "1" +  '*' * a + str(a + 1)
    return cadena

if __name__ == "__main__":
    """ 
    Función principal, para probar la función pattern().
    """
    ejemplos = [2, 4, 10]
    for numero in ejemplos:
        print(f"n = {numero}")
        print(f"{pattern(numero)}")

