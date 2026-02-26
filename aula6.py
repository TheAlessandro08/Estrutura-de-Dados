#Definimos o saldo inicial da conta
saldo=500.0
print(f"*** BEM-VINDO AO BANCO PYTHON ***\nSaldo atual: R$ {saldo:.2f}")

#Iniciamos o laço que manterá o caixa "ligado"
while saldo>0:
    #Solicitamos o valor do saque e convertemos para float
    saque=float(input("\nQuanto deseja sacar? (ou digite 0 para sair): "))

    #1. Verificação de saída: se digitar 0, o 'break' encerra o programa
    if saque==0:
        print("Operação finalizada. Volte sempre!")
        break

    #2. Verificação de saldo: não podemos sacar mais do que temos
    if saque<=saldo:
        #O operador '-=' subtrai o valor do saque do saldo atual
        saldo-=saque
        print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
        print(f"Saldo restante: R$ {saldo:.2f}")
    else:
        #Se o saque for maior que o saldo, exibimos um alerta
        print(f"Saldo insuficiente! Você só tem R$ {saldo:.2f}")

    #Se o saldo chegar a zero, o loop 'while saldo > 0' termina sozinho
    if saldo==0:
        print("\nSua conta está zerada. O sistema será desligado")