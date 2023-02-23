#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

#Recebe a velocidade que o usuario informa.
velocidade = float(input('Qual a velocidade atual do carro? ').strip())

#Calculo da multa
multa = (velocidade - 80) * 7

#Se a velocidade for maior ou = a 80 sem multa, caso contrario calcula a multa e exibe.
if velocidade <= 80:
    print(f' Tenha um bom dia, dirija com segurança! ')
else:
    print(f' Você foi multado, excedeu o limite permitido que é 80Km/h. ')
    print(f' Você deve pagar uma multa de R${multa:.2f}. ')
    print(f' Tenha um bom dia, dirija com segurança. ')