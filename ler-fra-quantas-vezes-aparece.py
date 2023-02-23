#Desafio: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

#Recebe frase do usuario.
frase = input("Digite uma frase: ").upper().strip()

#Conta quantas letras A.
cont = frase.count("A")
#Procura a primeira posição da letra A com find, como a primeira posição inteira é 0, soma +1 para que mostre como posição 1.
procure = frase.find("A")+1
#Procura a primeira posição da direita com rfind, soma +1 para não contar o 0.
final = frase.rfind("A")+1

#Exibe os resultados.
print(f'A letra A aparece {cont} vezes.')
print(f'A letra A apareceu na posição {procure}.')
print(f'A letra A apareceu na posição {final}. ')