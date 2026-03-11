def calcular_media(lista_numeros):
    #Verifica se a lista não está vazia para evitar divisão por zero
    if not lista_numeros:
        return 0
    
    #Calcula a soma de todos os itens
    soma = sum(lista_numeros)
    
    #Descobre a quantidade de itens
    quantidade = len(lista_numeros)
    
    #Retorna o cálculo da média
    return soma / quantidade

meus_numeros = [10, 20, 30, 40, 50]
resultado = calcular_media(meus_numeros)

print(f"A média dos números é: {resultado}")