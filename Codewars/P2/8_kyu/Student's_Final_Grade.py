"""
Nombre: Rebeca Gregorio Espina.
Fecha: 9 de mayo del 2025.
Descripción:
Descripción:
Crea una función finalGrade, que calcula la nota final de un alumno en función de dos parámetros: una nota del
examen y un número de proyectos completados.
Esta función debe tomar dos argumentos:
examen - calificación del examen (de 0 a 100); proyectos - número de proyectos completados (de 0 en adelante);

Esta función debe devolver un número (calificación final). Hay cuatro tipos de calificaciones finales:
100, si la nota del examen es superior a 90 o si el número de proyectos completados es superior a 10.
90, si la nota del examen es superior a 75 y si el número de proyectos completados es mínimo 5.
75, si la nota del examen es superior a 50 y si el número de proyectos completados es mínimo 2.
0, en otros casos
Ejemplos (Entradas --> Salida):
    100, 12 --> 100
    99, 0 --> 100
    10, 15 --> 100
    85, 5 --> 90
    55, 3 --> 75
    55, 0 --> 0
    20, 2 --> 0
"""
from random import randint

def final_grade(exam, projects):
    """
    Función para determinar la nota final de un alumno de acuerdo a la nota del examen
    y al número de proyectos completados.
    :param exam: Nota del examen (0-10).
    :param projects: Número de proyectos completados (0-50).
    :return: Nota final del alumno.
    """
    # 100, si la nota del examen es superior a 90 o si el número de proyectos completados es superior a 10.
    if exam > 90 or projects > 10:
        nota_final = 100
    # 90, si la nota del examen es superior a 75 y si el número de proyectos completados es mínimo 5.
    elif exam > 75 and projects >= 5:
        nota_final = 90
    # 75, si la nota del examen es superior a 50 y si el número de proyectos completados es mínimo 2.
    elif exam > 50 and projects >= 2:
        nota_final = 75
    # 0, en otros casos
    else:
        nota_final = 0
    return nota_final

if __name__ == "__main__":
    """
    Función principal que asigna aleatoriamente la nota de examen y número de proyectos completados.
    """
    nota_examen = randint(0,100)    # Generar número entero aleatorio entre 0 y 100.
    proyecto_completado = randint(0,50) # Generar número entero aleatorio entre 0 y 50.
    print(f"{nota_examen}, {proyecto_completado} --> {final_grade(nota_examen, proyecto_completado)}")
