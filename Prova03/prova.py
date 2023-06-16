from pathlib import Path

parent_path = Path(__file__).parent
tarefas = Path(parent_path, 'tarefas.txt')
tarefas_concluidas = Path(parent_path, 'concluidas.txt')

class Tarefa:
  def __init__(self):
    self.pendentes = []
    self.concluidas = []
  
  def adicionar_tarefa(self, tarefa):
    self.pendentes.append(tarefa)
    
    arquivo = open(tarefas, 'a')
    arquivo.write(f'- {tarefa}\n')
    arquivo.close()
  
  def concluir_tarefa(self, tarefa):
    if tarefa not in self.pendentes:
      return None
    else:
      t = self.pendentes.index(tarefa)
      tarefa_concluida = self.pendentes.pop(t)
      self.concluidas.append(tarefa_concluida)
      
      arquivo = open(tarefas_concluidas, 'a')
      arquivo.write(f'- {tarefa_concluida}\n')
      arquivo.close()
  
  def exibir_proxima_tarefa(self):
    return self.pendentes[0]
  
  def exibir_todas(self):
    return self.pendentes
  
  def exibir_concluidas(self):
    return self.concluidas

t1 = Tarefa()
t1.adicionar_tarefa('Assistir Aulas Semana 03')
t1.adicionar_tarefa('Fazer Exercicios Semana 03')
t1.adicionar_tarefa('Assistir videos extras')
t1.adicionar_tarefa('Fazer Avaliacao semana 03')

print(t1.exibir_todas())
print(t1.exibir_proxima_tarefa())

t1.concluir_tarefa('Assistir Aulas Semana 03')
t1.concluir_tarefa('Fazer Exercicios Semana 03')

print(t1.exibir_concluidas())
print(t1.exibir_proxima_tarefa())
