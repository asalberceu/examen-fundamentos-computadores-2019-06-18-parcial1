# Un $n$-grama es una secuencia de $n$ caracteres consecutivos de una cadena.
# Escribir un programa que pregunte por una cadena y un número entero positivo $n$ y 
# muestre por pantalla todos los $n$-gramas de la cadena.

cadena= input('Introduce una cadena: ')
numero= int(input('Introduce un número positivo: '))

for letra in range( len(cadena)-2):
     ngramas=(cadena[letra:letra+numero])
     print(ngramas)
   

    
