"""
Nombre: Rebeca Gregorio Espina.
Fecha: 19 de marzo de 2025
Descripción:
Encapsulamiento
"""
# DIAGRAMA DE clases UML
# "#" Privado
# "+" Público

class CuentaBancaria:
    def __init__(self, titular:str, saldo_inicial:float=0): # ,0 : no hace falta mandar
        self.titular = titular
        self._saldo = saldo_inicial  # Para proteger agregar _ después de.

    def depositar(self, cantidad:float)-> None:
        ...

    def retirar(self, cantidad:float)-> None:
      ...
# Métodos get, set/ Métodos de acceso./ Encapsulamiento
    # Opción 1 get
    def get_saldo(self)-> float:
        return self._saldo
    # Opción 2 get
    @property   # Decorador propiedad
    def saldo(self)-> float:
        return self._saldo
    # Opción 1 set
    @saldo.setter
    def saldo(self, nuevo_saldo:float)-> None:
        self._saldo = nuevo_saldo


    # Método mágico
    def __str__(self) -> str:
        return f"Cuenta bancaria: (id = {self.no_id}, nombre = {self.nombre}, sueldo = {self.sueldo})"
        ...

if __name__=="__main__":
    cuenta_rebeca = CuentaBancaria("Rebeca",0)  # Puedo no mandar saldo
    cuenta_rebeca.saldo = 5
