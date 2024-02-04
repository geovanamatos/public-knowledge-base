#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar
# R$7,00 por cada Km acima do limite.


km=int(input('Qual é a velocidade atual do carro?'))
print('=-'*20)
if km <= 80:
    print("Parabens você está andando na velocidade permitida")
else:
    print("Multado! Você excedeu o limite permitido que e 80 km/h")
    n = (km-80)*7
    print('Você deve pagar uma multa de R$ {}!'.format(n))
    print('Tenha um bom dia! E dirija com segurança!')