# Escribir un programa que elimine de una lista dada todos los elementos repetidos 
# y muestre por pantalla los elementos de la lista sin repeticiones.

# Definimos una lista con repeticiones de prueba
lista = [2, 4, 8, 4, 1, 1, 1, 3, 8, 9, 8, 7, 8, 4, 2, 5, 1]
# Creamos otra lista vacía para ir añadiendo los elementos de la lista anterior sin repeticiones
lista_sin_repeticiones = []
# Recorremos los elementos de la lista inicial
for i in lista:
    # Comprobamos si el elemento no está en la lista sin repeticiones
    if i not in lista_sin_repeticiones: # El elemento no está en la lista sin repeticiones
        # Añadimos el elemento en la lista sin repeticiones
        lista_sin_repeticiones.append(i)
# Recorremos la lista sin repeticiones y mostramos sus elementos por pantalla.
for i in lista_sin_repeticiones:
    print(i)