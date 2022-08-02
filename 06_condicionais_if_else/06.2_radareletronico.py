'''
Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80km/h mostre uma mensagem na tela dizendo que ele foi multado.
A multa vai custar R$7,00 por km/h acima do limite. 
'''
from time import sleep

velocidade = float(input('Qual a sua velocidade atual? '))
print('Radar móvel')
print('Calculando velocidade')
print('*' * 2)
sleep(2)
print('*' * 4 )
sleep(2)
print('*' * 6)
sleep(2)
if velocidade <= 80:
    print('\033[1;32;47mDirija com segurança! Velocidade permitida nesta via é de 80 km/h\033[m')
else:
    print('Voce! foi multado!')
    print('Sua multa é de \033[1;31;40mR${:.2f}!\033[m'.format((velocidade - 80) * 7))
sleep(1)
print('Operação encerrada!')


