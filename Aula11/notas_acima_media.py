vet_notas = [0.0] * 10

notas_acima = 0
media = 0
soma = 0

for i in range(len(vet_notas)):
  vet_notas[i] = float(input(f'{i + 1}ª Nota: '))
  soma += vet_notas[i]

media = soma / len(vet_notas)

for i in range(len(vet_notas)):
  if(vet_notas[i] > media):
    notas_acima += 1

print(f'Media = {media}')
print('====================')
print(f'Qtde de notas acima da média: {notas_acima}')