lista = [1, 3, 4, 5, 3, 7, 5, 6 , 7]
nova_lista = []

for i in range(len(lista)):
  if lista[i] not in nova_lista:
    nova_lista.append(lista[i])

print(nova_lista)