'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a idade:
'''
from datetime import date

# Dados
atual = date.today().year
ano = int(input('Ano de nascimento do atleta? '))
idade = atual - ano

# Até 9 anos: Mirim
if idade <= 9:
    print('O atleta é da categoria Mirim.')
# Até 14 anos: Infantil
elif idade > 9 and idade <= 14:
    print('O atleta é da categoria Infantil.')
# Até 19 anos: Junior
elif idade > 14 and idade <= 19:
    print('O atleta é da categoria Junior.')
# Até 20 anos: Sênior
elif idade == 20:
    print('O atleta é da categoria Sênior.')
# Acima: Master
else: 
    print('O atleta é da categoria Master.')
