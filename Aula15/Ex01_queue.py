import queue as q

fila = q.Queue()

fila.put("A")
fila.put("B")
fila.put("C")

print('Tamanho fila: ', fila.qsize())

print(fila.get())
print(fila.get())
print(fila.get())

print('Fila está vazia? ', fila.empty())