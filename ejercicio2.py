# Escribir un programa para ver si un alumno ha aprobado o no un curso con dos exámenes parciales.
# Para aprobar el curso la nota media debe ser mayor o igual que 5 siempre y cuando en ambos parciales se tenga al menos un 4.

parcial1= float(input('introduzca nota primer parcial: '))
parcial2= float(input('introduzca nota segundo parcial: '))

media=(parcial1 + parcial2)/2

if media >= 5 and parcial1 >= 4 and parcial2 >= 4:
    print('aprobado, su media es ', media)
elif parcial1 < 4:
    print('suspenso, es el parcial 1 el que tienes que repetir por estar suspenso')
elif parcial2 < 4:
    print('suspenso, es el parcial 1 el que tienes que repetir por estar suspenso')


#if parcial1 or parcial2 < 4:
#    print('suspenso, ya que no llega al 4')
#    if parcial1 < 4:
#        print('es el parcial 1 el que tienes que repetir por estar suspenso')
#        if parcial1 < 4:
#            print('es el parcial 2 el que tienes que repetir por estar suspenso')
#elif parcial1 >= 4 and parcial2 >= 4:
#    media=(parcial1 + parcial2)/2
#    if media >= 5:
#        print('aprobado, su media es: ', media)
#    else:
#        print('suspenso')

