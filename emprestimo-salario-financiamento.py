# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.



valor_casa = float(input('Qual o valor da casa? R$').strip())
salario = float(input('Qual o seu salario? R$').strip())
anos = float(input('Em quantos anos quer pagar? ').strip())

parcela = valor_casa / (anos * 12)
porcent = salario * 30 / 100

if parcela <= porcent:
    print(f' Para pagar uma casa de R${valor_casa} em {anos}anos a prestação será de R${parcela:.2f}.')
    print(f' Empréstimo APROVADO. ')
else:
    print(f' Empréstimo negado. ')