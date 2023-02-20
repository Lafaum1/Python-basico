#Converte a temperatura de ºC para ºF

temp = float(input('Qual a temperatura em ºC?'))


#A formula abaixo é simplificada pois 9/5 é 1.8.

fah = temp * 1.8 + 32


print(f'A temperatura {temp}ºC corresponde a {fah:.1f}ºF. ')