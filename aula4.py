#Recebe a temperatura em Celsius e converte para número decimal (float)
celsius=float(input("Digite a temperatura em ºC: "))

#Fórmula de conversão: (C*9/5)+32
fahrenheit=(celsius*9/5)+32

#Exibe o resultado formatado
print(f"{celsius}ºC equivale a {fahrenheit}ºF")