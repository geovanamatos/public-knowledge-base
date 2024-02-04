#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome completo em maiusculas é {nome.upper()}')
print(f'Seu nome completo em minusculas é {nome.lower()}')
espacos = (nome.count(' '))
print(f'Seu nome tem ao todo {len(nome) - espacos} letras')
primeiro = nome.find(' ')
print(f'Seu primeiro nome tem {primeiro} letras.')