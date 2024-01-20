#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros 

medida=float(input('Uma distância em metros:'))
cm= medida*100
mm=medida*1000
print('A média de {}m correpsonde a {}cm e {}mm'.format(medida, cm, mm))