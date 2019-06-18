# Escribir un programa para ver si un alumno ha aprobado o no un curso con dos exámenes parciales.
# Para aprobar el curso la nota media debe ser mayor o igual que 5 siempre y cuando en ambos parciales se tenga al menos un 4.

parcial1 = int(input('Introduce la nota del primer parcial: '))
parcial2 = int(input('Introduce la nota del segundo parcial: '))
if parcial1 >= 5:
    print('Apto')
elif parcial1 < 5:
    print('No Apto')
if parcial2 >= 5:
    print('Apto')
elif parcial2 < 5:
    print('No Apto')