'''
Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
deles e escrevendo o nome do escolhido.

'''
import random

al1 = input('O nome do 1º aluno: ')
al2 = input('O nome do 2º aluno: ')
al3 = input('O nome do 3º aluno: ')
al4 = input('O nome do 4º aluno: ')  

lista = [al1, al2, al3, al4]
# Foi criada uma lista para facilitar o armazenamento dos dados de nomes, no python lista fica em []. 
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
# simplificando o programa: from random import choice, e remover o random. 
