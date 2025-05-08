"""
Nombre: Rebeca Gregorio Espina.
Fecha: 3 de abril de 2025.
Descripión:
Se desea desarrollar un sistema en Python para gestionar un torneo de fútbol en el que participan
varios equipos, y cada equipo está compuesto por jugadores.

6. Diseño del módulo principal (Main.py):
    Se requiere diseñar una interfaz en consola (menú) que permita:
    Crear nuevos jugadores y equipos, solicitando los datos requeridos para cada objeto.
    Ver lista de jugadores y equipos, mostrando la lista de todos los objetos.
    Agregar jugadores a algún equipo. En este caso, se debe mostrar un submenú que indique los jugadores para seleccionar, luego otro submenú que indique a qué equipo se quiere añadir. Nota: No se considera el caso de que un jugador pertenezca a dos equipos.
    Eliminar jugadores de un equipo. En este caso, se debe mostrar un submenú con la lista de equipos, después de seleccionar a alguno de ellos, se debe de mostrar la lista de jugadores a eliminar del equipo.
    Agregar equipos al torneo. En este caso, se debe mostrar un submenú que indique los equipos a añadir al torneo. Nota: no se considera el caso de que un equipo se inscriba más de una vez.
    Eliminar equipos del torneo. En este caso, se debe mostrar un submenú con la lista de equipos a remover del torneo.
    Anotar gol(es) a un jugador. En este caso, se debe solicitar la cantidad de goles a anotar y que escoja a un jugador (mostrando la lista).
    Conocer el número total de goles de los equipos. En este caso, se debe mostrar los goles totales de cada equipo.
    Generar rol de juegos. Generar un rol de juegos con los equipos del torneo estilo "todos contra todos" organizado por jornadas.
Nota: Se considera que se tiene un único objeto de la clase Torneo.
"""
from Jugador import Jugador
from Equipo import Equipo
from Torneo import Torneo

torneo = Torneo("Torneo A")
jugadores = []
equipos = []

def validar(v_numero:str)-> int|None:
    """
    Función que valida y convierte una cadena a entero positivo.
    :param v_numero: Cadena a validar.
    :return: Devuelve el entero convertido si es válido, None si no cumple con los requisitos.
    """
    if v_numero.isdigit():
        if v_numero.isdigit() and int(v_numero) >= 0:
            return int(v_numero)
        return None

def conseguir_valor(cad_numero:str)-> int:
    """
    Solicita un valor numérico(en forma de cadena) al usuario hasta que sea válido.
    :param cad_numero: Cadena a validar.
    :return: Entero positivo validado.
    """
    numero_aceptado = validar(cad_numero)
    while numero_aceptado is None:
        print("Intenta nuevamente.")
        cad_numero = input("Ingresa un número entero positivo: ")
        numero_aceptado = validar(cad_numero)
    return numero_aceptado


while True:
    """
    Menú principal para el torneo.
    """
    print("-- Bienvenido al torneo: Champions League --")
    print("1.   Crear nuevo jugador.")
    print("2.   Crear nuevo equipo.")
    print("3.   Ver lista de jugadores.")
    print("4.   Ver lista de equipos.")
    print("5.   Agregar jugadores a algún equipo.")
    print("6.   Eliminar jugadores de un equipo.")
    print("7.   Agregar equipos al torneo.")
    print("8.   Eliminar equipos del torneo.")
    print("9.   Anotar gol(es) a un jugador.")
    print("10.  Conocer el número total de goles de los equipos.")
    print("11.  Generar rol de juegos.")
    print("0.   Salir")

    opcion = input("Por favor, ingresa una de las opciones anteriores: ")

    if opcion == "0":
        print("Fin del programa...")
        break

    elif opcion == "1":
        print("-- Crear nuevo jugador --")
        nombre = input("Nombre del jugador: ")
        cadena_numero = input("Número del jugador: ")
        numero = conseguir_valor(cadena_numero) # Validar.
        jugador = Jugador(nombre, numero)   # Crear instancia de jugador.
        jugadores.append(jugador)   #Agregar a la lista.
        print(f"Jugador {nombre} se ha creado.")

    elif opcion == "2":
        print("-- Crear nuevo equipo --")
        nombre = input("Nombre del equipo: ")
        equipo = Equipo(nombre) # Crear instancia equipo.
        equipos.append(equipo)  # Agregar a la lista.
        print(f"Equipo {nombre} se ha creado;  ID={equipo.id_equipo}")

    elif opcion == "3":
        print("-- Ver lista de jugadores --")
        if not jugadores:
            print("No hay jugadores.")
        else:
            for jugador in jugadores:
                print(jugador)

    elif opcion == "4":
        print("-- Ver lista de equipos --")
        if not equipos:
            print("No hay equipos.")
            break
        else:
            for equipo in equipos:
                print(equipo)

    elif opcion == "5":
        print("-- Agregar jugadores a algún equipo --")
        if not jugadores or not equipos:
            print("Debes tener jugadores y equipos.")
        else:
            print("\nJugadores disponibles:")
            for con, jugador in enumerate(jugadores):
                print(f"{con + 1}. {jugador.nombre} (Número {jugador.numero})")

            cad_jugador = input("Selecciona el número del jugador a agregar: ")
            num_jugador = conseguir_valor(cad_jugador) - 1

            if 0 <= num_jugador < len(jugadores):
                jugador_seleccionado = jugadores[num_jugador]
                print("\nEquipos disponibles:")
                for i in range(len(equipos)):
                    print(str(i + 1) + ". " + equipos[i].nombre)

                cad_equipo = input("Selecciona el número del equipo: ")
                num_equipo = conseguir_valor(cad_equipo) - 1
                if 0 <= num_equipo < len(equipos):
                    # Agregar jugador al equipo seleccionado.
                    equipos[num_equipo].agregar_jugadores(jugador_seleccionado)
                    print(f"Jugador {jugador_seleccionado.nombre} agregado a {equipos[num_equipo].nombre}.")
                else:
                    print("Opción no válido.")
            else:
                print("Opción no válido.")
# Los equipos pueden agregar o remover jugadores, ya sea individualmente o en grupos.
    elif opcion == "6":
        print("-- Eliminar jugadores de un equipo --")
        if not equipos:
            print("No hay equipos registrados")
        else:
            print("\nEquipos disponibles:")
            for i in range(len(equipos)):
                equipo = equipos[i]
                print(str(i + 1) + ". " + equipo.nombre)
            cad_equipo=input("Selecciona el número del equipo: ")
            num_equipo = conseguir_valor(cad_equipo) - 1
            if 0 <= num_equipo < len(equipos):
                equipo_seleccionado = equipos[num_equipo]

                if not equipo_seleccionado.jugadores:
                    print("Este equipo no tiene jugadores para eliminar.")
                else:
                    print("\nJugadores en el equipo:")
                    for i in range(len(equipo_seleccionado.jugadores)):
                        jugador = equipo_seleccionado.jugadores[i]
                        print(str(i + 1) + ". " + jugador.nombre + " (Número " + str(jugador.numero) + ")")
                    cad_jugador = input("Selecciona el número del jugador a eliminar: ")
                    num_jugador = conseguir_valor(cad_jugador) - 1
                    if 0 <= num_jugador < len(equipo_seleccionado.jugadores):
                        equipo_seleccionado.remover_jugadores(equipo_seleccionado.jugadores[num_jugador])
                        print("Jugador eliminado del equipo.")
                    else:
                        print("Opción no válido.")
            else:
                print("Opción no válido.")
# Los torneos pueden agregar o remover equipos, ya sea individualmente o en grupos.
    elif opcion == "7":
        print("-- Agregar equipos al torneo --")
        if not equipos:
            print("No hay equipos disponibles.")
        else:
            for equipo in equipos:
                torneo.agregar_equipos(equipo)
            print(f"Se agregaron {len(equipos)} equipos al torneo.")

    elif opcion == "8":
        print("-- Eliminar equipos del torneo --")
        if len(torneo.equipos) > 0:
            torneo.mostrar_equipos()
            nombre_equipo = input("Ingrese el nombre del equipo que desea eliminar del torneo o enter para salir: ")

            while nombre_equipo:
                for equipo in torneo.equipos:
                    if equipo.nombre == nombre_equipo:
                        torneo.eliminar_equipo(equipo)
                        print("Se eliminó correctamente.")

                nombre_equipo = input("Nombre del equipo a eliminar del torneo o 'ENTER' para salir: ")
        else:
            print("No se hay equipos del torneo que eliminar.")
    elif opcion == "9":
        print("-- Anotar gol(es) a un jugador --")
        if not jugadores:
            print("No hay jugadores")
        else:
            print("Jugadores disponibles")
            for i in range(len(jugadores)):
                print(f"{i + 1}. {jugadores[i].nombre} (Número {jugadores[i].numero})")
            cad_jugador = input("Selecciona el número del jugador: ")
            num_jugador = conseguir_valor(cad_jugador)-1
            if 0 <= num_jugador < len(jugadores):
                cad_goles = input("Cantidad de goles a anotar: ")
                goles = conseguir_valor(cad_goles)
                jugadores[num_jugador].anotar_goles(goles)
                print(f"Goles actualizados para {jugadores[num_jugador].nombre}.")
            else:
                print("Opción no válida.")

    elif opcion == "10":
        print("-- Conocer el número total de goles de los equipos --")
        if not equipos:
            print("No hay equipos.")
        else:
            for equipo in equipos:
                print(f"{equipo.nombre}: {equipo.total_goles()} goles")

    elif opcion == "11":
        print("-- Generar rol de juegos --")
        torneo.generar_rol()
    else:
        print("Opción no válido.")
    print()