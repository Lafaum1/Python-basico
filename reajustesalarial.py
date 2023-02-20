#Calcula o reajuste salarial, com aumento de 15%.

salario = float(input('Qual o seu salario atual? '))

# Calculo de porcentagem multiplica e depois divide por 100, logo após soma com salario atual.
reajuste = salario + (salario*15/100)

print(f'O salario de R${salario} com o reajuste de 15% ficará {reajuste:.2f}. ')