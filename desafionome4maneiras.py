#Desafio: crie um programa que transforme o nome digitado pelo usuario em todas letras, maiusculas, minusculas
#Conte todas as letras subtraindo os espaços e por ultimo apareça somente o primeiro nome

nome = input('Qual o seu nome completo? ')


#todas as letras maiusculas
print(nome.upper())

#todas as letras minusculas
print(nome.lower())

#len conta quantos caracteres tem na frase, replace substitui/remove os espaços por nada.
print(len(nome.replace(" ","")))

#split cria uma lista, [0] puxa primeira palavra, se for 1 puxa segunda palavra.
prim_nome = nome.split()[0]
print(prim_nome)