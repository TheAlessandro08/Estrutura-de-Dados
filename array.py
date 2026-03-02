def exibir_menus():
    print("\n--- MENU LISTA DE COMPRAS ---")
    print("1. Adicionar item")
    print("2. Remover item")

    print("3.Exibir lista")
    print("4.Sair")

def sistema_compras():
    # Criando o array vazio (lista)
    lista_compras= []

    while True:
        exibir_menus()
        opcao=input("Escolha uma opção (1-4): ")

        if opcao == "1":
            item=input("Digite o nome do produto: ")
            lista_compras.append(item) # .append() adiciona ao final do array
            print(f"'{item}' foi adicionado com sucesso!")

        elif opcao == "2":
            if not lista_compras:
                print("A lista está vazia! Nada para remover.")
            else:
                print("\nItens atuais:", lista_compras)
                item_remover=input("Qual item deseja remover? ")

                if item_remover in lista_compras:
                    lista_compras.remove(item_remover)
                    print(f"'{item_remover}' removido!")
                else:
                    print("Erro: Item não encontrado na lista.")

        elif opcao == "3":
            print("\n--- SUA LISTA ATUAL ---")
            if not lista_compras:
                print("A lista está vazia.")
            else:
                #Usamos enumerate para mostrar o índice (0,1,2,...)
                for i, item in enumerate(lista_compras):
                    print(f"{i}.{item}")

        elif opcao == "4":
            print("Saindo... Boas compras!")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

# Iniciar o programa
if __name__ == "__main__":
    sistema_compras()