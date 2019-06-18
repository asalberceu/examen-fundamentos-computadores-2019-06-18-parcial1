# Escribir un programa para ver si un alumno ha aprobado o no un curso con dos exámenes parciales.
# Para aprobar el curso la nota media debe ser mayor o igual que 5 siempre y cuando en ambos parciales se tenga al menos un 4.

#A lo largo de un curso se realizan dos exámenes parciales. Para aprobar el curso la nota media debe ser mayor o igual que 5 siempre y cuando en ambos parciales se tenga al menos un 4. Escribir un programa que pregunte al usuario la nota de los dos parciales y muestre por pantalla si el alumno ha aprobado el curso o si no, y en caso de no haber aprobado, qué parcial tiene que repetir por tener menos de 4 en él.
#Nota: Utilizar el fichero ejercicio2.py .

parcial1= float(input('Introduce la nota del parcial 1: '))
parcial2= float(input('Introduce la nota del parcial 2: '))

if parcial1<4:
    print('El alumno tiene que recuperar el primer parcial por haber sacado menos de un 4')
if parcial2<4:
    print('El alumno tiene que recuperar el segundo parcial por haber sacado menos de un 4')

if parcial1>=4 and parcial2>=4:
    notamedia = int((parcial1 + parcial2)/ 2)
    if notamedia >= 5:
        print('El alumno ha aprobado el primer curso')
    else:
     print('El alumno no ha superado el primer curso')
