#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


#Puxa informações do usuario.
num_1 = int(input('Qual o primeiro número? ').strip())
num_2 = int(input('Qual o segundo número? ').strip())
num_3 = int(input('Qual o terceiro número? ').strip())

# Calculo de maior número com if, elif e else.
if num_1 > num_2 and num_1 > num_3:
    print(f' O maior número é {num_1}. ')
elif num_2 > num_1 and num_2 > num_3:
    print(f' O maior número é o {num_2}. ')
else:
    print(f' O maior número é o {num_3}. ')

# Calculo de menor número com if, elif e else.
if num_1 < num_2 and num_1 < num_3:
    print(f' O menor número é o {num_1}.')
elif num_2 < num_1 and num_2 < num_3:
    print(f' O menor número é o {num_2}.')
else:
    print(f' O menor número é o {num_3}.')