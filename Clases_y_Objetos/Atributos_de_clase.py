"""
Nombre: Rebeca Gregorio Espina.
Fecha: 5 de marzo de 2025
Descripión:
"""
class Empleado:
    no_id = 1
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
        self.no_id = Empleado.no_id
        Empleado.no_id += 1

    #def aumentar_sueldo(self, nombre:str, sueldo:float )-> None:

    def __str__(self) -> str:
        return f"Empleado: (id = {self.no_id}, nombre = {self.nombre}, sueldo = {self.sueldo})"

if __name__=="__main__":
    print(Empleado.no_id)
    rebeca = Empleado("Rebeca",40)

    print(rebeca)