#Lista de números inteiros
numeros = [2, 5, 8, 11, 14, 17, 20, 23]

#Variável para contar quantos pares encontramos
contador_pares = 0

# Percorrer a lista com um laço for
for numero in numeros:
    #Usar o operador % para verificar se é par
    if numero % 2 == 0:
        contador_pares += 1  #Incrementa o contador

#Exibir o resultado final
print(f"Foram encontrados {contador_pares} números pares na lista.")