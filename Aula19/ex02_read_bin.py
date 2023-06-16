from pathlib import Path
import struct

parent_path = Path(__file__).parent
file_path_in = Path(parent_path, 'tentativas.bin')

arquivo = open(file_path_in, 'rb')

conteudo = arquivo.read()

print(conteudo)

arquivo.close()