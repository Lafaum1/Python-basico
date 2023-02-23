#Desafio: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

#Puxa o nome do usuario, exclui os espaços e transforma a primeira letra de cada nome em maiuscula.
nome = input('Qual o nome todo? ').strip().title()

#Cria uma lista com o nome informado.
lista = nome.split()
#Puxa o primeiro item da lista, na posição 0.
primeiro = lista[0]
#Puxa o ultimo nome da lista, na posição -1.
ultimo = lista[-1]

#Exibe os resultados.
print(f'Prazer em te conhecer.')
print(f'Seu primeiro nome é {primeiro}.')
print(f'Seu ultimo nome é {ultimo}')
