"""
Nombre: Rebeca Gregorio Espina.
Fecha: 9 de mayo del 2025.
Descripción:
Todo el mundo conoce la clásica regla de citas de
"la mitad de tu edad más siete" que mucha gente sigue (incluyéndome a mí). Es la edad recomendada para salir con alguien.
    Mínimo = (Edad / 2) + 7
    Máximo= 2 * ( Edad - 7 )
    Edad mínima ≤ Su edad ≤ Edad máxima

Tarea
Dado un número entero (1 <= n <= 100) que representa la edad de una persona, devuelve su rango de edad mínimo y máximo.
Esta ecuación no funciona cuando la edad <= 14, así que si la edad <= 14, utilice esta ecuación en su lugar:
    min = age - 0.10 * age
    max = age + 0.10 * age

Debes reducir todas tus respuestas para que se proporcione un entero en lugar de un punto flotante (que no representa la edad).
Devuelve tu respuesta en el formato "[min]-[max]"
Ejemplos:
    age = 27   =>   "20-40"
    age = 5    =>   "4-5"
    age = 17   =>   "15-20"
"""
from random import randint

def dating_range(age: int) -> str:
    """
    Función para calcular el rango de edad recomendado para citas según la regla de citas de "la mitad de tu edad más siete".
    :param age: Entero positivo que representa la edad.
    :return: Cadena con el rango de edades en formato "[min]-[max]".
    """
    if age <= 14:
        minimo = age - 0.10 * age
        maximo = age + 0.10 * age
    else:
        minimo = (age / 2) + 7
        maximo = 2 * (age - 7)
    return f"{int(minimo)}-{int(maximo)}"

if __name__ == "__main__":
    """
    Función principal, genera una edad aleatoria entre 0 y 100, manda calcular el rango de cita
    y finalmente muestra el resultado.
    """
    edad = randint(0,100)    # Edad aleatoria entre 0-100.
    print(f"age = {edad} --> '{dating_range(edad)}'")