'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
'''

n = str(input('Digite aqui o seu nome completo: ')).strip()  # strip() = fatia uma string
nome = n.split()   # split() = separa strings em substrings e retorna como lista
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu sobrenome é {}'.format(nome[len(nome)-1])) # nome, conta quantas strings tem a string nome e coloca -1, desta forma sempre retorna o sobrenome independente do tamanho do nome. 




