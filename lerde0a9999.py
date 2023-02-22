# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.


# Recebe o número digitado
num_1 = input('Digite um número: ')

# Converte para inteiro e puxa o dígito da casa indicada.
unid = int(num_1[0])

# Verifica se a string tem pelo menos dois caracteres antes de acessar o segundo caractere. Caso contrario ele exibe 0
if len(num_1) >= 2:
    dez = int(num_1[1])
else:
    dez = 0

# Verifica se a string tem pelo menos três caracteres antes de acessar o terceiro caractere. Caso contrario ele exibe 0
if len(num_1) >= 3:
    cen = int(num_1[2])
else:
    cen = 0

# Verifica se a string tem pelo menos quatro caracteres antes de acessar o quarto caractere. Caso contrario ele exibe 0
if len(num_1) >= 4:
    mil = int(num_1[3])
else:
    mil = 0

# Exibe as informações
print(f'Analisando o número {num_1}. ')
print(f'A unidade do número digitado é {unid}. ')
print(f'A dezena do número digitado é {dez}. ')
print(f'A centena do número digitado é {cen}. ')
print(f'A unidade de milhar é {mil}. ')