# Lista de exemplo
numeros = [12, 45, 7, 89, 32, 54]

# Vamos assumir que o primeiro elemento é o maior
maior_numero = numeros[0]

# Percorremos a lista comparando cada elemento
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero  # Atualiza o trono do maior número

# Exibe o resultado
print(f"O maior número encontrado na lista foi: {maior_numero}")