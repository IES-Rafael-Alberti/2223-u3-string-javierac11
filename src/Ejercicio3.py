#Ejercicio 3.0.3¶
#Tienes este código:
"""
palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador)
"""
#Encapsúlalo en una función llamada cuenta, y hazla genérica de 
#tal modo que pueda aceptar una cadena y una letra como argumentos.

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
    
def cuenta(cadena: str, letra: str):
    """Cuenta el numero de letras indicadas de la cadena

    Args:
        cadena (str): Es cualquier cadena de texto
        letra (str): Es cualquier caracter de 1 de longitud

    Returns:
        int: El numero de la letra introducida que tenga la cadena
    """
    cont = 0
    for letra_cadena in cadena:
        if letra_cadena == letra:
            cont += 1
    return cont

def generaMensaje(cadena: str, letra: str, cantidad_letra: int):

    return f"{cadena} tiene {cantidad_letra} {letra}"
    

if __name__ == "__main__":
    try:
        cadena = leeCadena()
        letra = leeLetra()
        
        numero_letras = cuenta(cadena, letra)
        
        print(generaMensaje(cadena, letra, numero_letras))
        
    except:
        print("Error")
        exit()
        