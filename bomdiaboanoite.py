#O programa dá Bom dia/Boa tarde/Boa noite de acordo com o horario que o usuario informa.

nome = input('Qual o seu nome? ')
horas = input('Que horas são? ')


if int(horas) >= 1 and int(horas) <= 11:
    print(f'Bom dia {nome}.')
elif int(horas) >= 12 and int(horas) < 18:
    print(f' Boa tarde {nome}.')
elif int(horas) >= 18:
    print(f'Boa noite {nome}.')
elif horas == ('00'):
    print(f'Boa noite {nome}. ')
else:
    print('Sem resultado conclusivo.')