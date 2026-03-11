#Funções para cada operação 
def somar(a, b):
    #Retorna a soma de dois números.
    return a + b

def subtrair(a, b):
    #Retorna a diferença entre dois números.
    return a - b

def multiplicar(a, b):
    #Retorna o produto de dois números.
    return a * b

def dividir(a, b):
    #Retorna o quociente, tratando a divisão por zero.
    if b == 0:
        return "Erro! Não é possível dividir por zero."
    return a / b

#Fluxo Principal do Programa

print("=== Minha Calculadora ===")

#Recebendo os dados do usuário
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

opcao = input("\nDigite o número da operação (1/2/3/4): ")

#Lógica de escolha
if opcao == '1':
    resultado = somar(n1, n2)
    print(f"\nResultado: {n1} + {n2} = {resultado}")
elif opcao == '2':
    resultado = subtrair(n1, n2)
    print(f"\nResultado: {n1} - {n2} = {resultado}")
elif opcao == '3':
    resultado = multiplicar(n1, n2)
    print(f"\nResultado: {n1} * {n2} = {resultado}")
elif opcao == '4':
    resultado = dividir(n1, n2)
    print(f"\nResultado: {n1} / {n2} = {resultado}")
else:
    print("\nOpção inválida! Tente novamente.")