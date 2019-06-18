# Un $n$-grama es una secuencia de $n$ caracteres consecutivos de una cadena.
# Escribir un programa que pregunte por una cadena y un número entero positivo $n$ y 
# muestre por pantalla todos los $n$-gramas de la cadena.

palabra = input('Introduce una palabra: ')
n = int(input('Introduce un número entero positivo: '))
for i in (range(len(palabra) - n + 1)):
    print(palabra[i:i+n])

