# Escribir un programa para ver si un alumno ha aprobado o no un curso con dos exámenes parciales.
# Para aprobar el curso la nota media debe ser mayor o igual que 5 siempre y cuando en ambos parciales se tenga al menos un 4.

nota_parcial1 = float(input("introduce la nota del primero parcial: "))
nota_parcial2 = float(input("introduce la nota del segundo parcial: "))
media = (nota_parcial1 + nota_parcial2)/2
if media >= 4:
    print("has aprobado el curso!!")
elif media < 4:
    if nota_parcial2 < 4 and nota_parcial1 >= 4:
        print("No has aprobado el segundo parcial, por lo tanto tienes que repetirlo.")
    if nota_parcial1 < 4 and nota_parcial2 >= 4:
        print("No has aprobado el primer parcial, por lo que tienes que repetirlo.")
    if nota_parcial1 < 4 and nota_parcial2 < 4:
        print("no has aprobado ningun parcial por lo que tienes que repetir los dos.")
