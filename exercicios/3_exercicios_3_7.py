print('Escreva um programa que leia a quandade de dias,horas, minutos e segundos do usuario. Calcule o toral em segundos.')

dias = float(input('Digite a  quantidade de dias:'))
horas = float(input('Digite a  quantidade de Horas:'))
minutos = float(input('Digite a  quantidade de Minutos e segundos:'))

calculo = int(dias*24) * (horas*3600) *(minutos*60)
print(f'Voce levou cerca de {calculo}segundos')