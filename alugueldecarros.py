#O programa calcula quanto o usuario vai pagar no aluguel do carro
#sendo que R$60 é por cada dia com o carro e R$0,15 por cada km percorrido.

dias = float(input('Quantos dias alugado? '))
kmrod = float(input('Quantos km rodados? '))

dias_1 = dias * 60 #Quantidade de dias alugado x valor por dia R$60
kmrod_1 = kmrod * 0.15 #Quantidade de km rodados x valor por km
soma1 = kmrod_1 + dias_1 #formula final

print(f' O total a pagar é R${soma1:.2f}. ')