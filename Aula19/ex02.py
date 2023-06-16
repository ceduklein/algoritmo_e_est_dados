import random
from pathlib import Path
import struct

parent_path = Path(__file__).parent
file_path_in = Path(parent_path, 'tentativas.bin')

arquivo = open(file_path_in, 'wb')

numero = random.randint(1, 10)

erros = []

tentativa = int(input('Tente adivinhar um número entre 1 e 10: '))

while tentativa != 0 and tentativa != numero:
  erros.append(tentativa)
  tentativa = int(input('Tente adivinhar um número entre 1 e 10: '))
  
if(tentativa == numero):
  print(f'Acertô Mizeravi! - Tentativa: {tentativa} - Número: {numero}')
  buf = struct.pack('%sf' % len(erros), *erros)
  arquivo.write(buf)
  print(erros)
   
else:
  print('Desistiu Mizaravi!')
  
arquivo.close()