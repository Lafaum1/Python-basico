#Converte de reais para dollar e euro.

moeda = float(input('Quanto você tem? '))

dolar = moeda / 5.17
euro = moeda / 5.52
arred_d = round(dolar, 2) # arredonda para 2 casas decimais
arred_e = round(euro, 2)

print(f'Com R${moeda} você conseguirá comprar US${arred_d} ou €{arred_e}. ')