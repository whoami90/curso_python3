'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

'''
import random

al1 = input('O nome do primeiro aluno: ')
al2 = input('O nome do segundo aluno: ')
al3 = input('O nome do terceiro aluno: ')
al4 = input('O nome do quarto aluno: ')
# Criação da lista de alunos
alunos = [al1, al2, al3, al4]
# Abaixo o aluno escolhido:
random.shuffle(alunos)
# A função shuffle serve para sortear sem excluir e montar uma lista aleatória, diferente de choice que escolhe um.
print('A ordem de apresentação será: ')
print(alunos)
# Para simplificar o programa basta: from random import shuffle
