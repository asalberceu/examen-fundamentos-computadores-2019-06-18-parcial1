# Escribir un programa para ver si un alumno ha aprobado o no un curso con dos exámenes parciales.
# Para aprobar el curso la nota media debe ser mayor o igual que 5 siempre y cuando en ambos parciales se tenga al menos un 4.

nota1 = float(input('Introduce la nota de la primera parte: '))
nota2 = float(input('Introduce la nota de la segunda parte: '))
if nota1 >= 4 and nota2 >= 4:
    if ((nota1 + nota2) / 2) >= 5:
        print('Has aprobado')
    else:
        print('Has suspendido')
if nota1 < 4:
    print('Tienes que repetir el primer parcial')
if nota2 < 4:
    print('Tienes que repetir el segundo parcial')
