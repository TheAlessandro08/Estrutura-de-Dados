class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.head = None

    def exibir_frutas(self):
        #Percorre a lista de frutas do início ao fim.
        atual = self.head
        
        print("--- Iniciando a travessia da lista ---")
        
        while atual is not None:
            # Imprime o dado do nó atual
            print(f"Fruta encontrada: {atual.dado}")
            
            # Pula para o próximo "vagão"
            atual = atual.proximo
            
        print("--- Chegamos ao fim da lista! ---")


minha_lista = ListaLigada()

no1 = No("Maçã")
no2 = No("Banana")
no3 = No("Cereja")

# Conectando a 'head' e os nós seguintes
minha_lista.head = no1
no1.proximo = no2
no2.proximo = no3

# Chamando o método para percorrer
minha_lista.exibir_frutas()