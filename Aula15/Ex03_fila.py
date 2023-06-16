class Fila:
  def __init__(self):
    self.items = []
    
  def esta_vazia(self):
    return len(self.items) == 0
  
  def primeiro_item(self):
    return self.items[0]
  
  def enfileirar(self, item):
    self.items.append(item)
  
  def desenfileirar(self):
    if self.esta_vazia():
      return None

    return self.items.pop(0)


fila = Fila()
fila.enfileirar('A')
fila.enfileirar('B')
fila.enfileirar('C')

print(f'Primeiro item: {fila.primeiro_item()}')
print('======================================')
item1 = fila.desenfileirar()
print('Item removido: ', item1)
item2 = fila.desenfileirar()
print('Item removido: ', item2)
item3 = fila.desenfileirar()
print('Item removido: ', item3)
  
print('======================================')
print('Fila está vazia? ', fila.esta_vazia())
print('======================================')
  