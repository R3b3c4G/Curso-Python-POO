"""
Nombre: Rebeca Gregorio Espina.
Fecha: 18 de marzo de 2025
Descripción:
    Los niños beben ponche.
    Los adolescentes beben Coca-Cola.
    Los adultos jóvenes beben cerveza.
    Los adultos beben whisky.
Crear una función que reciba la edad y devuelva lo que beben.

Normas:
    Niños menores de 14 años.
    Adolescentes menores de 18 años.
    Joven menor de 21 años.
    Los adultos tienen 21 o más.

Ejemplos: (Entrada --> Salida)
    13 --> "drink toddy"
    17 --> "drink coke"
    18 --> "drink beer"
    20 --> "drink beer"
    30 --> "drink whisky"
"""

def cadena_a_entero(cadena):
    no_guiones = cadena.count("-")
    revisar_cadena =cadena.lstrip('-')

    if revisar_cadena.isnumeric() and no_guiones in (0, 1):
        return int(cadena)
    else:
        return None

def people_with_age_drink(age)-> str:
    if age < 14:
        return "drink toddy"
    elif 14 <= age < 18:
        return "drink coke"
    elif 18 <= age < 21:
        return "drink beer"
    elif age >= 21:
        return "drink whisky"

if __name__ == "__main__":
    cadena_edad = input("Ingresa tu edad: ")
    edad = cadena_a_entero(cadena_edad)
    while edad is None:
        print("Opción no válida, intenta nuevamente.")
        print()
        cadena_edad= input("Ingresa tu edad: ")
        edad = cadena_a_entero(cadena_edad)
    print(edad," --> ",people_with_age_drink(edad))
