# Un $n$-grama es una secuencia de $n$ caracteres consecutivos de una cadena.
# Escribir un programa que pregunte por una cadena y un número entero positivo $n$ y 
# muestre por pantalla todos los $n$-gramas de la cadena.

# Pedimos al usuario que introduzca una palabra y un número entero positivo
palabra = input('Introduce una palabra: ')
n = int(input('Introduce un número entero positivo: '))
# Recorremos las posiciones de la palabra desde el inicio hasta la longitud de la palabra menos n + 1. 
# No tiene sentido seguir ya que las subcadenas después de esa posición tendrían longitud menor que n.
for i in (range(len(palabra) - n + 1)):
    # Mostramos el n-grama que empieza en la posición i
    print(palabra[i:i+n])
