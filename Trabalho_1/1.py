class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.head = None

    def imprimir_lista(self):

        atual = self.head
        
        if atual is None:
            print("A lista está vazia.")
            return

        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo  # Move para o próximo nó
        print("None")

# Criando a lista e os nós
minha_lista = ListaLigada()
minha_lista.head = No(10)
no2 = No(20)
no3 = No(30)

# Ligando os nós
minha_lista.head.proximo = no2
no2.proximo = no3

# Chamando o método
minha_lista.imprimir_lista()
