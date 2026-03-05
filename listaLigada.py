class Nodo: 
    def __init__(self,dado):
        self.dado=dado
        self.proximo=None

class ListaLigada:
    def __init__(self):
        self.cabeca=None

    def inserir_no_inicio(self,novo_dado):
        novo_nodo=Nodo(novo_dado)
        novo_nodo.proximo=self.cabeca
        self.cabeca=novo_nodo

    def imprimir_lista(self):
        atual=self.cabeca
        while atual:
            print(f"[{atual.dado}] ->",end="")
            atual=atual.proximo
        print("None")

minha_lista=ListaLigada()

minha_lista.inserir_no_inicio("Capítulo 3")
minha_lista.inserir_no_inicio("Capítulo 2")
minha_lista.inserir_no_inicio("Capítulo 1")

minha_lista.imprimir_lista()