text = 'Hello World!'

def contador_caracter(text):
  dic = {}

  for char in text:
    if char in dic:
      dic[char] += 1
    else:
      dic[char] = 1

  return dic
    
print(contador_caracter(text))
