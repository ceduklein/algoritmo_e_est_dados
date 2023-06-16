from dataclasses import dataclass

@dataclass
class Livros:
  titulo: str = ''
  autor: str = ''
  ano: str = ''
  
l1 = Livros("Dona Flor e seus dois maridos", "Jorge Amado", "1985")
l2 = Livros("Dom Casmurro", "Machado de Assis", "1977")
l3 = Livros("Código da Vinci", "Dan Brown", "1998")

print(f'{l1.titulo} - {l1.autor}')
print(f'{l2.titulo} - {l2.autor}')
print(f'{l3.titulo} - {l3.autor}')