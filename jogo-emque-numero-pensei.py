#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

#Importa biblioteca random
import random
import time

#Exibe mensagem inicial
print('-=-' * 20)
print(f'Vou pensar em um número de 0 a 5, tente advinhar.')
print('-=-' * 20)
print(f'PROCESSANDO...')
#3 segundos até aparecer o input
time.sleep(3)
#Recebe número do usuario.
numero = int(input('Em que número eu pensei? ').strip())

#Usa randint para pensar em um número inteiro aleatorio de 0 a 5.
computador = random.randint(0,5)


#Se acertar o número do computador, exibe que acertou, se não exibe que errou.
if numero == computador:
    print(f'Pensei no número {computador}.')
    print(f'Acertouu, parabéns. ')
else:
    print(f'Pensei no número {computador}. ')
    print(f'Eroooooooooooooooooooooou!')



