#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”.


#Recebe o nome da cidade, usa o strip para eliminar todos os espaços.
cidade = input('Em que cidade você nasceu? ').strip()

#Primeiro ler as 5 primeiras letras, depois transforma tudo em maiusculo.
print(cidade[:5].upper() == 'SANTO')