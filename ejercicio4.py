# Escribir un programa que elimine de una lista dada todos los elementos repetidos 
# y muestre por pantalla los elementos de la lista sin repeticiones.

# Lista de ejemplo
lista = [2, 4, 8, 4, 1, 1, 1, 3, 8, 9, 8, 7, 8, 4, 2, 5, 1]


# Debe mostrar 2, 4, 8, 1, 3, 9, 7, 5 
lista2 = []
for i in lista:
    if i not in lista2:
        lista2.append(i)
print(lista2)