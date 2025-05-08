"""
Nombre: Rebeca Gregorio Espina.
Fecha: 9 de mayo del 2025.
Descripción:
Tome un array y elimine cada segundo elemento. Conserve siempre el primer elemento y comience a eliminar con el siguiente.
Ejemplo:
    ["Keep", "Remove", "Keep", "Remove", "Keep", ...]-->["Keep", "Keep", "Keep", ...]
    ¡Ninguna de las matrices estará vacía, por lo que no tienes que preocuparte por eso!
"""
def remove_every_other(my_list:list) -> list:
    """
    Función para eliminar cada segundo elemento de un array. Conserva siempre el primer elemento y comienza a eliminar al siguiente.
    :param my_list: Lista de carácteres ingresados por el usuario.
    :return: Nueva lista con cada primer elemento conservado.
    """
    nueva_lista = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            nueva_lista.append(my_list[i])
    return nueva_lista

if __name__ == "__main__":
    """
    Función principal que solicita cadena, los guarda como lista y manda a eliminar cada segundo elemento de la lista.
    """
    arrays = []
    cadena = input("Ingresa tu cadena: ")
    while not cadena:
        cadena = input("Ingresa tu cadena: ")
    while cadena:
        arrays.append(cadena)
        cadena = input("Ingresa tu siguiente cadena o presione (ENTER) para salir: ")
    print(f"{arrays} --> {remove_every_other(arrays)}")