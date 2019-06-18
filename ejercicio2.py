# Escribir un programa para ver si un alumno ha aprobado o no un curso con dos exámenes parciales.
# Para aprobar el curso la nota media debe ser mayor o igual que 5 siempre y cuando en ambos parciales se tenga al menos un 4.
Nota1 = float(input('Que nota tienes en el primer parcial?'))
Nota2 = float(input('Que nota tienes en el segundo parcial?'))
if Nota1 < 4: 
    print('Tienes que hacer otra vez el primer parcial')
    if Nota2<4 :
        print('tienes que hacer otra vez el 2 parcial')
if Nota1 >= 4 and Nota2 >= 4:
    Media = (Nota1+Nota2)/2 
    if Media >= 5:
        print('A')
    else:
        print('S')
