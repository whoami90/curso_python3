"""
Crie um programa que leia o nome completo de uma pessoa e mostre: 
> O nome com todas as letras maiusculas.
> Quantas letras ao todo (sem considerar os espaços).
> Quantas letras tem o primeiro nome. 

"""

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome ...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras ao todo'.format(len(nome) - nome.count(' ')))
# len vai ler os espaços tambem, para resolver isso pode remover os espaçoes durante o input, assim vai eliminar os espaços antes e depois
# Para eliminar os espaços entre as palavras bast utilizar -nomedastring.count('')
# O ultimo problema: 
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
# Para separar cada um dos nomes: 
separa = nome.split()
print(separa)
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
# No exemplo acima o separa é uma lista onde o nome completo é quebrado para poder trabalhar com cada elemento separadamente. 

