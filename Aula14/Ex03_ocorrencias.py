lista = [0] * 10

alvo = int(input("Informe número alvo: "))
ocorrencias = 0

for i in range(len(lista)):
  lista[i] = int(input('Informe um número para lista: '))
  
  if alvo == lista[i]:
    ocorrencias += 1

print(alvo)
print(lista)
print(ocorrencias)  