# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo


# Exibe layout.
print('-=-'*20)
print('ANALISADOR DE TRIANGULOS')
print('-=-'*20)

# Puxa informações.
seg_1 = float(input('Qual o primeiro segmento? ').strip())
seg_2 = float(input('Qual o segundo segmento? ').strip())
seg_3 = float(input('Qual o terceiro segmento? ').strip())


# Condição para calcular se é ou não um triangulo.
if seg_1 < seg_2 + seg_3 and seg_2 < seg_1 + seg_3 and seg_3 < seg_1 + seg_2:
    print(f' Os segmentos podem formar um triângulo. ')
else:
    print(f' Os segmentos NÃO podem formar um triângulo.')
