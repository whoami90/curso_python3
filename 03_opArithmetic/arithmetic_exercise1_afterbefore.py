# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor. 

'''
Dados: um número fornecido pelo usuário
O que fazer com os dados: exibir na tela o número antecessor e o sucessor do número fornecido pelo usuário.
restrição: O usuário deve inserir um número inteiro.
O que é esperado do programa: Exibir na tela com a sintaxe : o {} antecede o número do usuário e o {} sucede o número. 

'''
num = int(input('Digite aqui um número: '))
a = num - 1
s = num + 1
print('O numero {} antecede o número do usuário e o {} sucede o número do usuário'.format(a, s))

