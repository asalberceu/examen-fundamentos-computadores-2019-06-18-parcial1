# Escribir un programa para ver si un alumno ha aprobado o no un curso con dos exámenes parciales.
# Para aprobar el curso la nota media debe ser mayor o igual que 5 siempre y cuando en ambos parciales se tenga al menos un 4.


nota1 = float(input('Cual fue tu nota del primer parcial?:  '))
nota2 = float(input('Cual fue tu nota del segundo parcial?:  '))
media=(nota1+nota2)/2
if media < 5:
    print('Has suspendido')
else:
    print('Has aprobado')



if nota1 <= 4: 
    print('Debes repetir el primer examen')
if nota2 <=4 :
        print('Debes repetir el segundo examen ')
