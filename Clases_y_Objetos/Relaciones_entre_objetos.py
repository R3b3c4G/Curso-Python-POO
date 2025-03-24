"""
Nombre: Rebeca Gregorio Espina.
Fecha: 19 de marzo de 2025
Descripción:
Parte 2 de empleado_sueldo
"""
class Empleado:
    no_id = 1
    def __init__(self, nombre:str, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
        self.no_id = Empleado.no_id
        Empleado.no_id += 1

    #def aumentar_sueldo(self, nombre:str, sueldo:float )-> None:

    def __str__(self) -> str:
        return f"Empleado: (id = {self.no_id}, nombre = {self.nombre}, sueldo = {self.sueldo})"

class Empresa:
    def __init__(self, nombre: str, *empleados: tuple[Empleado]):
        self.nombre = nombre
        self.empleados = list(empleados)    # Convertir tupla en lista

    def agregar_empleados(self, *nuevos_empleados:tuple[Empleado]):
        for empleado in list(nuevos_empleados):
            self.empleados.append(empleado)

    def mostrar_empleados(self) -> None:
        """
        Se utiliza para mostrar los empleados de la empresa en forma de lista.
        """
        print(f"*** Lista de empleados de {self.nombre} ***")
        for empleado in self.empleados:
            print(empleado)

    def __str__(self) -> str:
        # Se convierte los elementos de la lista en cadenas (invocando str() para cada uno de ellos) y
        # se unen con ", " a través del métod0 str.join().
        # Este patrón es muy común en Python para obtener una cadena a partir de una lista.
        empleados = ", ".join(str(empleado) for empleado in self.empleados)
        return f"Empresa: (Nombre: {self.nombre }, {empleados})"


if __name__=="__main__":
    rebeca = Empleado("Rebeca",40)
    empresa1 = Empresa("RG", rebeca)
    empresa1.mostrar_empleados()
    print()
    print(empresa1)
    print()
    print(rebeca)
    rebeca.nombre = ("Rebeca")
    print(rebeca)
    print(rebeca.nombre)