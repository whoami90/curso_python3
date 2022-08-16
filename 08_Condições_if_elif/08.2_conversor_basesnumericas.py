'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão

- 1 para binário.
- 2 para octal
- 3 para hexadecimal
'''

# Entrada de dados 
num = int(input('Digite um número inteiro: '))

print('''Escolha uma das opções abaixo: 
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')

opção = int(input('Sua opção: '))

# Tratamento de dados.

# Condicionais
if opção == 1:
    print('{} convertido para Binário é {}'.format(num, bin(num) [2:]))
elif opção == 2:
    print('{} convertido para Octal é {}'.format(num, oct(num) [2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é {}'.format(num, hex(num) [2:]))
else: 
    print('Opção invalida, tente novamente! ')