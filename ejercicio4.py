# Escribir un programa que elimine de una lista dada todos los elementos repetidos 
# y muestre por pantalla los elementos de la lista sin repeticiones.


l= []
pregunta= int(input('Introduce los elementos que quieras meter en la lista: '))
for i in range (pregunta):
    l.append(input('Introduce el elemento que quieres que vaya en la siguiente posición: '))
    print(l)

lsinrepetir = [] 
for i in l:
    if i not in lsinrepetir:
        lsinrepetir.append(i)  
        print(lsinrepetir)

