import random #Importa o módulo para gerar números aleatórios

#O computador escolhe um número entre 1 e 10
numero_secreto=random.randint(1,10)
tentativas=0

print("--- JOGO DA ADIVINHAÇÃO ---")
print("Tente adivinhar o número que eu pensei entre 1 e 10!")

while True:
    chute=int(input("Qual o seu palpite?"))
    tentativas += 1 #Soma 1 ao contador de tentativas

    if chute == numero_secreto:
        print(f"ACERTOU! Você precisou de {tentativas} tentativas.")
        break #Interrompe o laço while
    elif chute < numero_secreto:
        print("Mais alto... Tente novamente!")
    else:
        print("Mais baixo... Tente novamente!")