from collections import deque #Biblioteca para criar filas de forma eficiente

fila_atendimento=deque(["Ana","Bruno","Carlos"]) #Criando a fila

fila_atendimento.append("Daniel")#Enqueue: Chegou um novo cliente (Daniel)

cliente_atendido=fila_atendimento.popleft() #Dequeue: O primeiro da fila (Ana)

print(f"Atendendo agora: {cliente_atendido}")
print(f"Restam na fila: {list(fila_atendimento)}")