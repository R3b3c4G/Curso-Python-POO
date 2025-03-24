"""
Nombre: Rebeca Gregorio Espina.
Fecha: 5 de marzo de 2025
Descripión:
"""
# Clase: Primera letra mayúscula /
# Función: Letra minúscula o "_" como separador.

class Persona:
    # Método especial llamado constructor.
    def __init__(self, nombre:str, edad:int, altura:float, peso:float):
        # Atributos de mi persona
        self.nombre = nombre
        self.edad= edad
        self.estatura = altura
        self.peso = peso
        """
    # Métodos
    def caminar(self) -> None:
        print("Estoy caminando.")
    def comer(self):
        print("Estoy comiendo.")
    def jugar(self):
        print("Estoy jugando.")
    def dormir(self):
        print("Estoy durmiendo.")
    """

    def caminar(self) -> None:
        print(f"{self.nombre} está caminando para bajar sus {self.peso} Kgs.")  # Incluyenyendo el self. /autoreferencia al propio objeto.
    def comer(self):
        print(f"{self.nombre} está comiendo una manzana.")
    def jugar(self):
        print(f"{self.nombre} está jugando basquet.")
    def dormir(self):
        print(f"{self.nombre} está durmiendo.")




if __name__=="__main__":
    rebeca = Persona("Rebeca Gregorio Espina", 19, 157, 43.8) # Primer objeto
    # Acceder a los atributos del objeto Persona
    print(rebeca.nombre)
    print(rebeca.edad)
    print(rebeca.estatura)
    print(rebeca.peso)
    print("")
    rebeca.caminar()
    rebeca.comer()
    rebeca.jugar()
    rebeca.dormir()

    paty = Persona("Paty", 19, 1.60, 48)    # Nuevo objeto
    paty.caminar()
    paty.comer()
    print("")
    rebeca.edad = 20
    rebeca.peso = 56
    rebeca.caminar()
    print(rebeca.nombre)
    print()