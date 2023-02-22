#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# Recebe o número digitado
num_1 = int(input('Digite um número: '))

#Operação matématica
unid = num_1 // 1 % 10
dez = num_1 // 10 % 10
cen = num_1 // 100 % 10
mil = num_1 // 1000 % 10

# Exibe as informações
print(f'Analisando o número {num_1}. ')
print(f'A unidade do número digitado é {unid}. ')
print(f'A dezena do número digitado é {dez}. ')
print(f'A centena do número digitado é {cen}. ')
print(f'A unidade de milhar é {mil}. ')