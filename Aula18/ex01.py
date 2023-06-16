lista_numeros = [1,3,5,3,7,3,1,5,1,9,1]

def contar_itens(lista):
  contador = {}
  for item in lista:
    if item in contador:
      contador[item] += 1
    else:
      contador[item] = 1
      
  return contador

ocorrencias = contar_itens(lista_numeros)

for item, contador in ocorrencias.items():
  print(f'O número {item} aparece {contador} vez(es) na lista.')