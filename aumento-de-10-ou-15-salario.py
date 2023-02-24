#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
#calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

#Puxa informações do usuario.
salario = float(input('Qual o salario do funcionario? R$').strip())

# Se for maior que 1250 aplica 10% de aumento, caso contrario aplica 15%.
if salario > 1250:
    salario_porcent = salario * 10 / 100
    salario_final = salario_porcent + salario
    print(f' O salario {salario:.2f} com o aumento será R${salario_final:.2f}.')
else:
    salario_porcent = salario * 15 / 100
    salario_final = salario_porcent + salario
    print(f' O salario {salario:.2f} com aumento será R${salario_final:.2f}.')