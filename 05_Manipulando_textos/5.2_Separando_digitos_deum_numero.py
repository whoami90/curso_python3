"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. 

"""
# forma de utilização como string
num = int(input('Informe um número: '))
n = str(num)
print('Analisando o número {}'.format(num))
print('unidade é {}'.format(n[3]))
print('Dezena é {}'.format(n[2]))
print('Centena é {}'.format(n[1]))
print('Milhar é {}'.format(n[0]))
# Problema deste formato utilizado string é que se foi pedido 4 dígitos e for inserido um número de 3 dígitos ou menos o programa dá erro.
# Para ser possível a indexação de um número, primeiro o número inserido foi convertido para inteiro e depois convertido para uma variável string
# uma vez transformado em string basta utilizar a tecnica de indexação

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10 

print('Analisando o número {}'.format(num))
print('Unidade: {} '.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

