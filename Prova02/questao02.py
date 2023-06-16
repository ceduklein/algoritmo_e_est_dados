class ProcessamentoElementos:
  def __init__(self):
    self.fila = []
    self.pilha = []
  
  def enfileirar_elemento(self, elemento):
    self.fila.append(elemento)
  
  def empilhar_elemento(self, elemento):
    self.pilha.append(elemento)
  
  def processar_elementos(self):
    while len(self.pilha) > 0 or len(self.fila) > 0:
      if len(self.fila) > 0:
        print(self.fila.pop(0))
      if len(self.pilha) > 0:
        print(self.pilha.pop())
    
    print('Lista e Fila Vazias.')

processo = ProcessamentoElementos()

processo.enfileirar_elemento('A')
processo.enfileirar_elemento('B')
processo.enfileirar_elemento('C')

processo.empilhar_elemento('X')
processo.empilhar_elemento('Y')
processo.empilhar_elemento('Z')

processo.processar_elementos()
  
  
        
    
    