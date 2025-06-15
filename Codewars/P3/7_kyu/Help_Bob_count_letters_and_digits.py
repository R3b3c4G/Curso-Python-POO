"""
Nombre: Rebeca Gregorio Espina.
Fecha: 12 de junio del 2025.
Descripción:
Bob es un hombre perezoso.
Necesita que crees un método que pueda determinar cuántas letras
ASCIIletters (tanto mayúsculas como minúsculas ) y hay en una cadena determinada.digits
Ejemplo:
    "¡Hola!" --> 6
    "¡malvado...!" --> 6
    "!?..A" --> 1
"""

def count_letters_and_digits(s):
    """
    Función que cuenta cuántos carácteres son letras ASCII o dígitos en una cadena dada.
    :param s: Cadena a evaluar.
    :return: Número de carácteres que son letras o dígitos.
    """
    contador = 0
    for digito in s:
        # .isalpha() detecta letras (A-Z, a-z).
        # .isdigit() detecta dígitos (0-9).
        if digito.isalpha() or digito.isdigit():
            contador += 1
    return contador

"""
# Nota: Algunos ejemplos no son correctos
    # Ejemplos correctos:
        tests = [
            ('n!!ice!!123', 7),
            ('de?=?=tttes!!t', 8),
            ('', 0),
            ('!@#$%^&`~.', 0),
            ('u_n_d_e_r__S_C_O_R_E', 10),
        ]
"""

if __name__ == "__main__":
    """ 
    Función principal, para probar la función count_letters_and_digits().
    """
    print(f"¡Hola! --> {count_letters_and_digits("¡Hola!")}")
    print(f"¡malvado...! --> {count_letters_and_digits("¡malvado...!")}")
    print(f"!?..A --> {count_letters_and_digits("!?..A")}")