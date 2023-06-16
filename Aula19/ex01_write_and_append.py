from pathlib import Path

parent_path = Path(__file__).parent
file_path_in = Path(parent_path, 'write.txt')

arquivo = open(file_path_in, 'a')

arquivo.write('Ola Mundo SENAI!\n')

arquivo.close()

