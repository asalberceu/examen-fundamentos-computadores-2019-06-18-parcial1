# Un $n$-grama es una secuencia de $n$ caracteres consecutivos de una cadena.
# Escribir un programa que pregunte por una cadena y un número entero positivo $n$ y 
# muestre por pantalla todos los $n$-gramas de la cadena.

cadena = str(input("introduce una cadena: "))
numero = int(input("introduce un numero entero positivo"))
for i in range(len(cadena)-2):
    print(cadena[i:i+numero])
    