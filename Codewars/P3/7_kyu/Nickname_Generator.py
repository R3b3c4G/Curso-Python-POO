"""
Nombre: Rebeca Gregorio Espina.
Fecha: 12 de junio del 2025.
Descripción:
Generador de apodos
Escriba una función nickname_generator que tome un nombre de cadena como argumento y
devuelva las primeras 3 o 4 letras como apodo.

Si la tercera letra es una consonante, devuelve las primeras 3 letras.
    nickname("Robert") //=> "Rob"
    nickname("Kimberly") //=> "Kim"
    nickname("Samantha") //=> "Sam"

Si la tercera letra es una vocal, devuelve las primeras 4 letras.
    nickname("Jeannie") //=> "Jean"
    nickname("Douglas") //=> "Doug"
    nickname("Gregory") //=> "Greg"

Si la cadena tiene menos de 4 caracteres, devuelve "Error: Nombre demasiado corto".

Notas:
Las vocales son "aeiou", así que descuente la letra "y".
La entrada siempre será una cadena.
La entrada siempre tendrá la primera letra en mayúscula y el resto en minúscula (por ejemplo, Sam).
La entrada se puede modificar.
"""
def nickname_generator(name):
    """
    Función que genera un apodo a partir de un nombre dado.
    :param name: Cadena de texto del nombre con la primera letra en mayúscula.
    :return: Cadena con el apodo generado o un mensaje de error.
            - Si la tercera letra es una consonante, devuelve las primeras 3 letras.
            - Si la tercera letra es una vocal, devuelve las primeras 4 letras.
            - Si la cadena tiene menos de 4 caracteres, devuelve "Error: Name too short".
    """
    if len(name) < 4:
        # Si la cadena tiene menos de 4 caracteres, devuelve "Error: Name too short".
        return "Error: Name too short"
    elif name[2].lower() in 'aeiou':
        # Si la tercera letra es una vocal, devuelve las primeras 4 letras.
        return name[:4]
    # La tercera letra es una consonante, devuelve las primeras 3 letras.
    return name[:3]

if __name__ == "__main__":
    """ 
    Función principal, para probar la función nickname_generator().
    """
    print(f"Robert --> {nickname_generator("Robert")}")
    print(f"Jeannie...! --> {nickname_generator("Jeannie")}")
    print(f"Sam --> {nickname_generator("Sam")}")