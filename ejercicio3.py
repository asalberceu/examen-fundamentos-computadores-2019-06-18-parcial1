# Un $n$-grama es una secuencia de $n$ caracteres consecutivos de una cadena.
# Escribir un programa que pregunte por una cadena y un número entero positivo $n$ y 
# muestre por pantalla todos los $n$-gramas de la cadena.

palabra = input('Palabra: ')
numero = int(input('numero: '))
f1 = palabra.split(numero)
print(str(f1))