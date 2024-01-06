#Faça um programa que leia algo pelo teclado 
#e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

a=(input('Digite algo:'))
print(f'''
É Alpha númerico? {a.isalnum()},
É aplha? {a.isalpha()},
É Minuscula? {a.islower()},
É maiuscula? {a.isupper()},
Esta capitalizada? {a.istitle()},
É Decimal? {a.isdecimal()},
É numérica? {a.isnumeric()},
É espaço? {a.isspace()}
''')
