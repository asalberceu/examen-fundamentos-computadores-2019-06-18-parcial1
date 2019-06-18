# Escribir un programa para ver si un alumno ha aprobado o no un curso con dos exámenes parciales.
# Para aprobar el curso la nota media debe ser mayor o igual que 5 siempre y cuando en ambos parciales se tenga al menos un 4.
nota1= float(input("Nota del primer parcial: "))
nota2= float(input("Nota del segundo parcial: "))
if (nota1 >= 4 and nota2 >=4) and ((nota1+nota2)/2 >5):
    print("has aprobado")
else:
    print("no has aprobado")

