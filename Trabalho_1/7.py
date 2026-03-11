class No:
    #Representa um único nó em uma lista ligada.    
    #Atributos:
    #dado: O valor ou informação armazenada no nó.
    #proximo: Referência para o próximo nó da lista (inicialmente None).
    

    def __init__(self, dado):
        self.dado = dado      # O valor que queremos guardar
        self.proximo = None   # O "ponteiro" que aponta para o próximo Nó

# Criando três nós isolados
no1 = No("Maçã")
no2 = No("Banana")
no3 = No("Cereja")

# Conectando os nós (criando a corrente)
no1.proximo = no2
no2.proximo = no3

# Agora, a partir do no1, podemos chegar ao no3:
print(f"Início: {no1.dado}")
print(f"Próximo: {no1.proximo.dado}")
print(f"Depois do próximo: {no1.proximo.proximo.dado}")