class Carro:
  def __init__(self, marca, modelo, ano) :
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

class ListaCarros:
  def __init__(self):
    self.carros = []
  
  def adicionar(self, carro):
    self.carros.append(carro)
    
  def exibir_registros(self):
    for carro in self.carros:
      print(f'{carro.modelo} - {carro.ano}')

c1 = Carro("Honda", "Civic", 2017)
c2 = Carro("Renault", "Sandero", 2017)
c3 = Carro("Renault", "Kwid", 2019)

lista_carros = ListaCarros()
lista_carros.adicionar(c1)
lista_carros.adicionar(c2)
lista_carros.adicionar(c3)

lista_carros.exibir_registros()
