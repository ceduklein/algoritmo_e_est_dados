vet_numeros = [0] * 10
vet_par = []
vet_impar = []

for i in range(len(vet_numeros)):
  vet_numeros[i] = int(input(f'{i + 1}º Número: '))
  
  if(vet_numeros[i] % 2 == 0): 
    vet_par.append(vet_numeros[i])
  else:
    vet_impar.append(vet_numeros[i])

print(f'Números digitados: {vet_numeros}')
print('=======================================')
print(f'Números pares: {vet_par} - Qtde números pares: {len(vet_par)}')
print('=======================================')
print(f'Números ímpares: {vet_impar} - Qtde números ímpares: {len(vet_impar)}')
