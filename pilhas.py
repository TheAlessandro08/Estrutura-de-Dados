pilha=[]

pilha.append("Prato Limpo 1")
pilha.append("Prato Limpo 2")
pilha.append("Prato Limpo 3")
pilha.append("Prato Limpo 4")
pilha.append("Prato Limpo 5")
pilha.append("Prato Limpo 6")
pilha.append("Prato Limpo 7")
pilha.append("Prato Limpo 8")
pilha.append("Prato Limpo 9")
pilha.append("Prato Limpo 10")

print(f"Pilha após 3 entradas: {pilha}")

if pilha:
    topo=pilha[-1]
    print(f"O item que está no topo agora é: {topo}")

item_removido=pilha.pop()
print(f"Removendo do topo: {item_removido}")

print(f"Pilha atualizada: {pilha}")

if not pilha:
    print("A pilha está vazia.")
else:
    print(f"A pilha ainda tem {len(pilha)} itens.")