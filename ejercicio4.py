# Escribir un programa que elimine de una lista dada todos los elementos repetidos 
# y muestre por pantalla los elementos de la lista sin repeticiones.

# Lista de ejemplo


lista = [2, 4, 8, 4, 1, 1, 1, 3, 8, 9, 8, 7, 8, 4, 2, 5, 1]
repetidos = []
for i in lista:
    if i not in repetidos:
        repetidos.append(i)
print(repetidos)
# Debe mostrar 2, 4, 8, 1, 3, 9, 7, 5 
