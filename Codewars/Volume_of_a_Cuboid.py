"""
Nombre: Rebeca Gregorio Espina.
Fecha: 31 de marzo de 2025
Descripción:
Bob necesita una forma rápida de calcular el volumen de un cuboide rectangular con tres valores: length, widthy heightdel cuboide.
Escriba una función para ayudar a Bob con este cálculo.
El volumen del ortoedro se calcula, al igual que el de cualquier prisma recto, multiplicando el área de la base por la altura.
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

def get_volume_of_cuboid(length, width, height)-> float:
    if(length <= 0 or width <= 0 or height <= 0):
        return 0
    else:
        return length * width * height

if __name__ == "__main__":
        cadena_largo = input("Ingresa el largo del cuboide rectangular: ")
        largo = cadena_a_flotante(cadena_largo)
        while largo is None:
            print("Opción no válida, intenta nuevamente.")
            cadena_largo = input("Ingresa el largo del cuboide rectangular: ")
            largo = cadena_a_flotante(cadena_largo)

        cadena_ancho = input("Ingresa el ancho del cuboide rectangular: ")
        ancho = cadena_a_flotante(cadena_ancho)
        while ancho is None:
            print("Opción no válida, intenta nuevamente.")
            cadena_ancho = input("Ingresa el ancho del cuboide rectangular: ")
            ancho = cadena_a_flotante(cadena_ancho)

        cadena_altura = input("Ingresa la altura del cuboide rectangular: ")
        altura = cadena_a_flotante(cadena_altura)
        while altura is None:
            print("Opción no válida, intenta nuevamente.")
            cadena_altura = input("Ingresa la altura del cuboide rectangular: ")
            altura = cadena_a_flotante(cadena_altura)
        volumen = get_volume_of_cuboid(largo, ancho, altura)
        print(f"\nEl volumen del cuboide rectangular es: {volumen:.2f}")