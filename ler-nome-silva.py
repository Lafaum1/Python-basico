#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

#recebe nome do usuario e com strip elimina os espaços.
nome = input('Qual é o seu nome? ').strip()


#Puxa o nome silva para maiusculo e caso encontre mostra true, caso contrario mostra false.

if "SILVA" in nome.upper():
    print(f'Seu nome tem Silva? True')
else:
    print(f'Seu nome tem Silva? False')