#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta 
#necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m>2

larg=float(input('Qual é a largura da parede?'))
alt=float(input('Qual é  altura?'))
área=larg*alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}'.format(larg,alt,área))
tinta=área/2
print('Para pintar sua parede você precisará de {}ml de tinta'.format(tinta))