"""
Nombre: Rebeca Gregorio Espina.
Fecha: 9 de mayo del 2025.
Descripción:
Esta función debería devolver un objeto, pero no cumple su función. ¿Cuál es el problema?:
def mystery():
    results = {
    'sanity': 'Hello'}
    return
    results
"""

def mystery():
    """
    Forma correcta de la función del ejercicio.
    """
    results = {
    'sanity': 'Hello'}
    # Nota: Los códigos después de la línea de return ya no se ejecutan.
    return results

if __name__ == "__main__":
    print(mystery())