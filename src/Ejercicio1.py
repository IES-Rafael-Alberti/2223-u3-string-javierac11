#Ejercicio 3.0.1¶
#Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás
#hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.

def leeCadena():
    """Lee una cadena de texto y la devuelve"""
    cadena = input("Introduce una cadena: ")
    return cadena

def invierteCadena(cadena: str):
    """Invierte una cadena de texto
    
    Se le introduce una cadena de texto
    
    Te devuelve la cadena invertida
    
    """
    cadena_invertida = ""
    
    for letra in cadena[::-1]:
        cadena_invertida += letra
    return cadena_invertida

def generaMensaje(cadena_invertida: str):
    """Devuelve un str con formato para que el ususario lo vea por 
    pantalla"""

    return f"La palabra invertida es: {cadena_invertida}"

if __name__ == "__main__":
    cadena = leeCadena()
    cadena_invertida = invierteCadena(cadena)
    print(generaMensaje(cadena_invertida))