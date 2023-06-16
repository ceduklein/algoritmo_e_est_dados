class Produto:
  def __init__(self, nome, qtde, valor):
    self.nome = nome
    self.qtde = qtde
    self.valor = valor

class Estoque:
  def __init__(self):
    self.estoqu = []
  
  def adicionar_item(self, item):
    self.produtos.append(item)
  
  def remover_item(self, item):
    if item in self.produtos:
      self.produtos.remove(item)
  
  def listar(self):
    for i in range(len(self.produtos)):
      print('============================================')
      print(f'Item {i + 1}: {self.produtos[i].nome} - Qtde: {self.produtos[i].qtde} - Valor: {self.produtos[i].valor}')
          
  def atualizar_qtde(self, item, qtde):
    if item in self.produtos:
      item.qtde = qtde

p1 = Produto('Iphone 14', 3, 6000.00)
p2 = Produto('Samsumg S22', 5, 4500.00)
p3 = Produto('JBL Go 3', 7, 290.05)

estoque = Estoque()
estoque.adicionar_item(p1)
estoque.adicionar_item(p2)
estoque.adicionar_item(p3)
print('')
print('Lista após adição dos itens:')
estoque.listar()

estoque.remover_item(p2)
print('')
print('Lista após remoção de um item:')
estoque.listar()

estoque.atualizar_qtde(p3, 2)
print('')
print('Lista após alteração da quantidade de um item:')
estoque.listar()


        
      