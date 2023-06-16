lista = [0] * 5

for i in range(len(lista)):
  lista[i] = int(input('Informe um número: '))
  
lista_ordenada = sorted(lista)

print(lista, lista_ordenada)

if lista == lista_ordenada:
  print(True)
else:
  print(False)