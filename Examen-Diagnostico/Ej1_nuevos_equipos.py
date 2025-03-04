"""
Nombre: Rebeca Gregorio Espina.
Fecha: 4 de marzo de 2025
Descripción:
Este programa debe generar 6 nuevos equipos de 2 personas cada uno, pero con la restricción
de que no puede haber dos personas que ya estuvieron en el mismo equipo.
El curso tiene los siguientes equipos:
    Los Algoritmos Anarquistas: Héctor, Addi y Jesús Alberto.
    Los Hackers de Café: Tania, Patricia, Rebeca.
    Los Codificadores nocturnos: Jamileth, Bryan, Rosalinda.
    Los Ctrl+Z: Galilea, Jennifer, Juan.
"""
import random
def generar_integrante():
    # lista = ["Héctor", "Addi" , "Jesús Alberto","Tania", "Patricia" , "Rebeca","Jamileth", "Bryan", "Rosalinda", "Galilea", "Jennifer", "Juan"]
    # opciones = ([equipo1], [equipo2],[equipo],[equipo4])

    equipo1 = ["Héctor", "Addi" , "Jesús Alberto"]
    equipo2 = ["Tania", "Patricia" , "Rebeca"]
    equipo3 = ["Jamileth", "Bryan", "Rosalinda"]
    equipo4 = ["Galilea", "Jennifer", "Juan"]
    integrante1 = random.choice(equipo1)
    equipo1.remove(integrante1)
    integrante2 = random.choice(equipo2)
    equipo2.remove(integrante2)

    return integrante1, integrante2
equipoa = generar_integrante()
"""equipob = generar_integrante()
equipoc = 
equipod =
equipoe =
equipof =
"""



def equipo_formado ():
    """
    Función principal
    """
    print("     Equipo final: ")
    print(f"Equipo A: {equipoa}")
    """
    print(f"Equipo B: {equipob}")
    print(f"Equipo C: {equipoc}")
    print(f"Equipo D: {equipod}")
    print(f"Equipo E: {equipoe}")
    print(f"Equipo F: {equipof}")
    """



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    equipo_formado()


