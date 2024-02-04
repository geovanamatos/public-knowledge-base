#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores 
#a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salário = float(input('Qual é o salário do funcionário? R$'))

if salário <= 1250:
    print(f'Seu aumento será de R${(salário * 0.15):.2f} totalizando R${salário * 1.15:.2f}')
else:
    print(f'Seu aumento será de R${(salário * 0.10):.2f} totalizando R${salário * 1.10:.2f}')