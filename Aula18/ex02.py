palavras = ["amor", "roma", "mary", "armo", "coração", "orcam"]

def verificar_anagramas(palavras):
  contador = {}
  
  for palavra in palavras:
    contador[palavra] = []
  
  for i in range(len(palavras)):
    for j in range(len(palavras)):
      if sorted(palavras[i]) == sorted(palavras[j]):
        contador[palavras[i]].append(palavras[j])
  
  return(contador)

print(verificar_anagramas(palavras))
 
  
  
  