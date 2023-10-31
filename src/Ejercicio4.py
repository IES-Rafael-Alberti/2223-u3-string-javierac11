#Ejercicio 3.0.4¶
#Hay un método de cadenas llamado count que es similar a find. Lee la documentación de este método 
# en: * Métodos en ingles * Métodos en castellano
#y escribe el código necesario para invocar a este método y contar el número de veces que una letra 
# aparece en “banana”.

def leeCadena():
    """Lee una cadena de texto y la devuelve"""
    cadena = input("Introduce una cadena: ")
    return cadena

def leeLetra():
    """Lee una cadena de texto y la devuelve controlando que no sea de mas o menos de 1 caracter"""
    letra = input("Introduce una letra: ")
    if len(letra) == 1:
        return letra
    else:
        raise IndexError("No tiene la longitud adecuada")
    
def cuenta2(cadena: str, letra: str):
    """Cuenta el numero de letras indicadas de la cadena

    Args:
        cadena (str): Es cualquier cadena de texto
        letra (str): Es cualquier caracter de 1 de longitud

    Returns:
        int: El numero de la letra introducida que tenga la cadena
    """
    numero_letras = cadena.count(letra)
    return numero_letras

def generaMensaje(cadena: str, letra: str, cantidad_letra: int):
    
    return f"{cadena} tiene {cantidad_letra} {letra}"
    
if __name__ == "__main__":
    cadena = leeCadena()
    letra = leeLetra()
    total_letra = cuenta2(cadena, letra)
    
    print(generaMensaje(cadena, letra, total_letra))