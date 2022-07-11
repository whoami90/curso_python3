# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

'''
Dados: As duas notas do aluno.
O que fazer com estes dados: Calcular a média
Restrições: Deve ser inseridos números inteiros
O que se espera deste problema: Exibir na tela a média entre duas notas de um aluno. 
'''

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
med = (nota1 + nota2) / 2
print('A média das notas do aluno é {:1f}'.format(med))
