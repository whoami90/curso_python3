'''
Crie um programa que faça o computador jogar jokenpô com você.
'''
from random import randint
from time import sleep

# Dados
itens = ('Pedra' , 'Papel' , 'Tesoura') # Lista com os itens que serão utilizados no jogo, 0 = pedra, 1 = papel e 2 = tesoura
computador = randint(0, 2) # variável computador onde é gerado o valor aleatório que corresponde a jogada do computador. 
# print('O computador escolheu {}'.format(itens[computador])) # Teste sorteio computador
print(''' Suas Opções:
[ 0 ] Pedra
[ 1 ] Papel 
[ 2 ] Tesoura
''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=-' * 20)
print('computador jogou {}'.format(itens[computador])) # Teste output computador
print('jogador jogou {}'.format(itens[jogador]))       # Teste output jogador
print('-=-' * 11)
# Pedra quebra tesoura
if computador == 0: # Computador jogou pedra 
    if jogador == 0: # Jogador jogou pedra
        print('EMPATE!')
    elif jogador == 1: # Jogador jogou papel
        print('Jogador vence!')
    elif jogador == 2: # Jogador jogou tesoura
        print('Computador vence!')
    else: 
        print('Jogada inválida!')

elif computador == 1: # Computador jogou papel
    if jogador == 0: # Jogador jogou pedra
        print('Computador vence!')
    elif jogador == 1: # Jogador jogou papel
        print('EMPATE!')
    elif jogador == 2: # Jogador jogou tesoura
        print('Jogador VENCE!')
    else:
        print('Jogada inválida!')
 
elif computador == 2: # Computador jogou tesoura
    if jogador == 0: # Jogador jogou Pedra
        print('Jogador vence!')
    elif jogador == 1: # Jogador jogou papel
        print('Computador vence!')
    elif jogador == 2: # Jogador jogou tesoura
        print('EMPATE!')
    else:
        print('Jogada inválida')


# Atualizar este programa posteriormente utilizando emojis de pedra, papel e tesoura para otimizar o programa. 