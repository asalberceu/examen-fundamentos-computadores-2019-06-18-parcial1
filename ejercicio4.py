# Escribir un programa que elimine de una lista dada todos los elementos repetidos 
# y muestre por pantalla los elementos de la lista sin repeticiones.

# Lista de ejemplo
#lista = [2, 4, 8, 4, 1, 1, 1, 3, 8, 9, 8, 7, 8, 4, 2, 5, 1]


# Debe mostrar 2, 4, 8, 1, 3, 9, 7, 5 
lista1 = []
n = int(input('Cuantos numeros quieres meter en la lista? '))
for i in range(n):
    lista1.append(input('numero en la siguiente posicion?'))
print(lista1)
listasinrep = []
for i in lista1:
    if i not in listasinrep:
        listasinrep.append(i)
print(listasinrep)