# Escribir un programa para ver si un alumno ha aprobado o no un curso con dos exámenes parciales.
# Para aprobar el curso la nota media debe ser mayor o igual que 5 siempre y cuando en ambos parciales se tenga al menos un 4.

# Pedimos al usuario que introduzca las notas de las asignaturas y las convertimos en números reales
nota1 = float(input('Introduce la nota de la primera parte: '))
nota2 = float(input('Introduce la nota de la segunda parte: '))
# Comprobamos si ambas notas son mayores o iguales que 4 y si la media es mayor o igual que 5
if nota1 >= 4 and nota2 >= 4 and ((nota1 + nota2) / 2) >= 5:  # Las dos notas son mayores que 4 y la media mayor o igual que 5
    print('Has aprobado')
else: # La nota media es menor que 5 o alguna nota es menor que 4 (suspenso)
    print('Has suspendido')
    # Comprobamos si la primera nota es menor que 4
    if nota1 < 4:
        print('Tienes que repetir el primer parcial')
    # Comprobamos si la segunda nota es menor que 4
    if nota2 < 4:
        print('Tienes que repetir el segundo parcial')
