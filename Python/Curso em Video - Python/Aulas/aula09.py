#Fatiamento de uma string
frase='Curso em Vídeo Python'
print(frase)
#ou
frase='Curso em Video Python'
print(frase[9])
#ou
frase='Curso em Vídeo Pytthon'
print(frase[9:14])
#ou
frase='Curso em Vídeo Python'
print(frase[9:21:2]) #o :2 pula de 2 em dois
#ou
frase='Curso em Vídeo Python'
print(frase[:5]) #começa no ínicio
#ou
frase=='Curso em Vídeo Python'
print(frase[9::3]) #vai comecar no nove, ir até o final e pular de 3 em 3

#Ánalise de uma string
frase='Curso em Vídeo Python'
print(len(frase)) #comprimento da frase

frase='Curso em Vídeo Python'
print(frase.count('o')) #conta quantas letras 'o' minúsculo tem no programa
#ou
frase='Curso em Vídeo Python'
print(frase.count('o',0,13)) #conta quantas letras 'o' minúsculo tem do 0 ao 12 pois o 13 não conta

frase='Curso em Vídeo Python'
print(frase.find('deo')) #vai me dizer onde foi encontrada a posição 'deo'
#ou
frase='Curso em Vídeo Python'
print(frase.find('Android')) #quando o valor não existe o find te retorna -1

frase='Curso em Vídeo Python'
print('Curso'in frase)

#Transformação
frase='Curso em Vídeo Python'
print(frase.replace('Python','Android')) #replace troca/reposiciona

frase='Curso em Vídeo Python'
print(frase.upper()) #deixa tudo maiúsculo

frase='Curso em Vídeo Python'
print(frase.lower()) #deixa tudo minúsculo

frase='Curso em Vídeo Python'
print(frase.capitalize()) #deixa todos caracteres minúsculos, apenas o primeiro que não

frase='Curso em Vídeo Python'
print(frase.title()) #transforma em maiúsculo todos inicios de palavras

frase='  Aprenda Python  '
print(frase.strip()) #remove espaços inúteis no ínicio e final de string
#ou
frase='  Aprenda Python  '
print(frase.rstrip()) #remove apenas o lado direito, últimos espaços
print(frase.lstrip()) #remove apenas o lado esquerdo, ínicio

#Divisão
frase='Curso em Vídeo Python'
print(frase.split()) #split vai criar uma divisão no lugar dos espaços

frase=['Curso', 'em', 'Vídeo', 'Python']
print('-'.join(frase)) #junta quando está separado por divisão

