vetor = [0] * 10

for i in range(len(vetor)):
  vetor[i] = int(input(f'{i + 1}º Número:'))

for i in range(len(vetor)):
  for j in range(len(vetor) - 1 - i):
    if(vetor[j] > vetor[j+1]):
      vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

print('Vetor ordenado', vetor)