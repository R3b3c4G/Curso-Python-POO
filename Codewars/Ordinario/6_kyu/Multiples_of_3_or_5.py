"""
Nombre: Rebeca Gregorio Espina.
Fecha: 25 de junio del 2025.
Descripción:
Si enumeramos todos los números naturales menores de 10 que son múltiplos de 3 o 5,
obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.
Termina la solución para que devuelva la suma de todos los
múltiplos de 3 o 5 menores que el número pasado.
Además, si el número es negativo, devuelve 0.
Nota: Si el número es múltiplo de 3 y de 5, cuéntelo solo una vez.
"""

def solution(number):
    resultado = 0
    if number < 0:  # Para número negativo, devuelve 0.
        return resultado
    for a in range(number):
        if a % 3 == 0 or a % 5 == 0:    # Si el número es múltiplo de 3 o de 5, el valor se incluye a la suma.
            resultado += a
    return resultado

if __name__ == "__main__":
    # Función principal para probar la función solution()
    print(f"10 --> {solution(10)}")
    print(f"-1 --> {solution(-1)}")