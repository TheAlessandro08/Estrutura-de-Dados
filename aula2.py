#Entrada de dados
#Pedindo os números ao usuário
#Usamos float() para aceitar números decimais (ex: 5.5)
num1=float(input("Digite o primeiro número: "))
num2=float(input("Digite o segundo número: "))

#Realizando o cálculo
soma=num1+num2

#Exibindo o resultado usando f-string (uma forma elegante de formatar texto)
print(f"A soma entre {num1} e {num2} é igual a {soma}")