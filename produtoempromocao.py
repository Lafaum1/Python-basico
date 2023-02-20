#Calcula o produto com desconto de 5%

preco = float(input('Qual o preço do produto? '))

#calcular porcentagem, primeiro multiplica depois divide por 100.
mult = preco * 5
divid = mult / 100
final = preco - divid

print (f'O produto de preço R${preco} com desconto de 5% ficará R${final:.2f}. ')