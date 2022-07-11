'''
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. 

Exemplo: Digite um número: 6.127
O número 6.127 tem a parte inteira 6

'''
# Este programa pode ser resolvido de várias formas diferentes
'''
import math
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(
    num, math.trunc(num)))

'''
# esta foi a primeira forma de resolver.

# Na importação acima foi importada toda a biblioteca math, caso quisesse apenas a função trunc =
# from math import trunc e retirar o math. de dentro do format senão dá erro.
# Outra forma de resolver é:

num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
# Nem sempre é necessário importar módulos. E o problema ainda é simples de resolver.
