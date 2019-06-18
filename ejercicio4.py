lista = [2, 4, 8, 4, 1, 1, 1, 3, 8, 9, 8, 7, 8, 4, 2, 5, 1]
numerosrepetidos = []
for i in lista:
  if not i in numerosrepetidos:
    numerosrepetidos.append(i)
print(numerosrepetidos)