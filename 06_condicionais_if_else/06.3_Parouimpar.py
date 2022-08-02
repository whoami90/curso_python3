'''
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar. 
'''

numero = int(input('Digite um número: '))
num = numero % 2
if num == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é impar'.format(num))

# Para resolver este problema é simples, apenas usando a lógica matemática de que apenas números pares podem ser divididos por 2, o resto será 0
# caso o resto seja um número diferente de 0, o número é impar. 
