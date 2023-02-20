#Calcular quanto de tinta vai usar com alturaxlargura de uma parede
#Sendo 1litro por cada 2m²


altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura
tinta = area / 2
arredond_t = round(tinta, 2)

print(f'As dimensões da sua parede é {altura}x{largura} e sua area é de {area}m²')
print(f'Você precisará de {arredond_t}l para pintar a sua parede. ')