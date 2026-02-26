nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))

#Processamento
media=(nota1+nota2)/2

#Saída com Condicional (Opcional para avançar)
if media>=7:
    print(f"Sua média foi {media}. Você está aprovado!")
else:
    print(f"Sua média foi {media}. Você precisa estudar mais para a recuperação.")