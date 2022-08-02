'''
Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá exibir na tela se o usuário venceu ou perdeu. 
'''
from random import randint # da biblioteca random importado somente randint (número inteiro aleatorio) 
from time import sleep # Função sleep da biblioteca time serve para fazer aguardar. 

computador = randint(0, 5) # Faz o computador 'pensar'
print('---=---' * 10)
print('Vou pensar em um número entre 0 e 5, tente adivinhar qual é. ')
print('Pensei no número ...')
print('---=---' * 10)
sleep(2)
numero = int(input('Agora me fala, em que número eu pensei? ')) # Jogador tenta adivinhar. 
print('Processando a resposta .')
sleep(2)      # esta função serve para fazer o programa aguardar a dar o proximo passo. 
print('Processando a resposta ..')
sleep(2)
print('Processando a resposta ...')
sleep(3)
if numero == computador: 
    print('Parabens acertou!')
else:
    print('Errou!')
print('Eu pensei no número {}'.format(computador))

