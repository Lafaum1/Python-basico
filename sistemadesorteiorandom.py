import random

#Recebe informações do usuario.
aluno1 = input('Qual o aluno 1? ')
aluno2 = input('Qual o aluno 2? ')
aluno3 = input('Qual o aluno 3? ')
aluno4 = input('Qual o aluno 4? ')
aluno5 = input('Qual o aluno 5? ')

#Faz a lista de alunos.
lista = [aluno1, aluno2, aluno3, aluno4, aluno5]

#Usa a bib random para escolher um aluno aleatoriamente
escolhe = random.choice(lista)

#exibe para o usuario a escolha.
print(f'O aluno escolhido foi {escolhe}. ')