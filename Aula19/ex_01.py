from pathlib import Path

parent_path = Path(__file__).parent
file_path_in = Path(parent_path, 'ola.txt')

arquivo = open(file_path_in, 'r')

print(arquivo.read())

arquivo.close()