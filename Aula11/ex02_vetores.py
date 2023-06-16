numeros = [0] * 10
soma = 0

for i in range(len(numeros)):
  numeros[i] = int(input(f'{i + 1}º Número: '))
  
  soma += numeros[i]

print(numeros)
print('==============================')
print(soma)
print('==============================')

maior_numero = numeros[0]
indice = 1

for indice in range(len(numeros)):
  if numeros[i] > maior_numero:
    maior_numero = numeros[i]

print (maior_numero)
  