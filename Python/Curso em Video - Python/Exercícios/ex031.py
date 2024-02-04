#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 
#por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distância = int(input('Qual a distância da viagem? '))
p1 = distância * 0.50
p2 = distância * 0.45
if distância <=200:
    print('O preço da passagem ficará R${:.2f}' .format(p1))
else:
    print('O preço da passagem ficará R${:.2f}' .format(p2))