class Pilha:
    def __init__(self):
        # Usamos uma lista interna para guardar os dados
        self.itens = []

    def push(self, item):
        #Adiciona um elemento ao topo da pilha.
        self.itens.append(item)
        print(f"Item {item} adicionado.")

    def pop(self):
        #Remove e retorna o elemento do topo. 
        #Se a pilha estiver vazia, avisa o usuário.
        if not self.esta_vazia():
            return self.itens.pop()
        else:
            print("Erro: A pilha está vazia!")
            return None

    def esta_vazia(self):
        #Verifica se a pilha não possui elementos.
        return len(self.itens) == 0

    def ver_topo(self):
        #Apenas mostra qual é o elemento no topo sem removê-lo.
        if not self.esta_vazia():
            return self.itens[-1]
        return None
    
minha_pilha = Pilha()

# Adicionando elementos (Push)
minha_pilha.push("Ação 1: Digitar texto")
minha_pilha.push("Ação 2: Negritar")
minha_pilha.push("Ação 3: Mudar cor")

print(f"\nO topo atual é: {minha_pilha.ver_topo()}")

# Removendo elementos (Pop)
print(f"\nRemovendo: {minha_pilha.pop()}")
print(f"Removendo: {minha_pilha.pop()}")

print(f"\nNovo topo após remoções: {minha_pilha.ver_topo()}")