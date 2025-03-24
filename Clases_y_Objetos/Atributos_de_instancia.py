"""
Nombre: Rebeca Gregorio Espina.
Fecha: 5 de marzo de 2025
Descripión:
"""
class Estudiante:   # Clase
    def __init__(self, nombre): # Constructor
        self.nombre = nombre
        self.temas_aprendidos = []

    def aprender_tema(self, tema:str) -> None:
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre} aprendió {tema}")

    # Para evitar: <__main__.Estudiante object at 0x00000192F3496E40>
    def __str__(self) -> str:  # Devuelve un texto
        return f"Estudiante (nombre:{self.nombre}, temas_aprendidos:{self.temas_aprendidos})"

class Profesor:
    def __init__(self, nombre:str, temas_dominados:list[str]) ->None:
        self.nombre = nombre
        self.temas_dominados = temas_dominados

    def dominar_tema(self, tema:str) ->None:
        self.temas_dominados.append(tema)

    def ensenar_tema(self, no_tema: int) -> str:
        if no_tema < len(self.temas_dominados):
            return self.temas_dominados[no_tema]
        else:
            return "Fuera de rango"

    def __str__(self) -> str:  # Devuelve un texto
        return f"Profesor (nombre:{self.nombre}, temas_dominados:{self.temas_dominados})"







if __name__=="__main__":
    rebeca = Estudiante("Rebeca")
    rosalinda = Estudiante("Rosalinda")
    rebeca.aprender_tema("Evolución sitios web")
    rosalinda.aprender_tema("Internet de las cosas")

    print(rebeca)
    print(rosalinda)

    alberto = Profesor("Alberto",["Atributos de instancia", "Clases", "Objetos"])
    alberto.dominar_tema("Y")
    print("")
    print(alberto)
    print(alberto.ensenar_tema(1))
    # Alternativa: tema1 = alberto.ensenar_tema(1)
    rebeca.aprender_tema(alberto.ensenar_tema(1))
    rosalinda.aprender_tema(alberto.ensenar_tema(2))

# Atributos de instancia: Variables que describen las características de un objeto y que pertenecen a una clase
# Instancia; Crear objeto con sus propios atributos



