"""
Nombre: Rebeca Gregorio Espina.
Fecha: 31 de marzo de 2025
Descripción:
Dado un número n, dibuje unas escaleras usando la letra "I", (n) alta y (n) ancha, con la más alta en la parte superior izquierda.
Por ejemplo n = 3 el resultado es:
"I\n I\n  I"

o impreso:
I
 I
  I

Otro ejemplo, una escalera de 7 escalones se debe dibujar así:
I
 I
  I
   I
    I
     I
      I
"""

def draw_stairs(n):
    stairs = ""
    for i in range(n):
        stairs += " " * i + "I"
        if i != n - 1:
            stairs += "\n"
    return stairs

def cadena_a_entero(cadena):
    no_guiones = cadena.count("-")
    revisar_cadena =cadena.lstrip('-')

    if revisar_cadena.isnumeric() and no_guiones in (0, 1):
        return int(cadena)
    else:
        return None

if __name__ == "__main__":
    cadena_numero = input("Ingresa un número entero: ")
    numero_escalon = cadena_a_entero(cadena_numero)
    while numero_escalon is None:
        print("Opción no válida, intenta nuevamente.")
        print()
        cadena_numero = input("Ingresa un número entero: ")
        numero_escalon = cadena_a_entero(cadena_numero)
    print(draw_stairs(numero_escalon))


