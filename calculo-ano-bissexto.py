#Calcule se o ano é BISSEXTO ou não.


#Recebe o ano que o user digitou.
ano = int(input('Que ano quer analisar? ').strip())

#Se for divisivel por 4 resto 0 e divisivel por 100 resto diferente de 0 ou divisivel por 400 resto 0, o ano é bissexto, caso contrario não é.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f' O ano é BISSEXTO.')
else:
    print(f' O ano não é BISSEXTO. ')