# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

#Puxa informação digitada pelo usuario.
distancia = float(input('Qual a distancia da viagem? ').strip())

#Calculos
menor = distancia * 0.50
maior = distancia * 0.45

#Se for menor ou igual a 200km cobramos 50centavos por km de viagem, se for maior que 200km cobramos 45centavos por Km.
if distancia <= 200:
    print(f'Você está prestes a começar uma viagem de {distancia}Km. ')
    print(f'E o preço da sua passagem custará R${menor:.2f}. ')
else:
    print(f'Você está prestes a começar uma viagem de R${distancia}Km. ')
    print(f'E o preço da sua passagem custará R${maior:.2f}. ')