'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: 
'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

# - O primeiro valor é maior
if n1 > n2: 
    print('O primeiro número é {} e é maior que o segundo'.format(n1))
# - O segundo valor é maior
elif n2 > n1:
    print('O segundo número é {} e é maior que o primeiro'.format(n2))
# - Não existe valor maior, os dois são iguais.
else:
    print('Ambos são iguais')


