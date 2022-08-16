'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
 -- > Seu programa também deve mostrar quanto tempo que falta ou que passou do prazo. 
'''
from datetime import date

# Dados
atual = date.today().year
nascimento = int(input('ano de nascimento: '))
idade = atual - nascimento
# - Se ele ainda vai se alistar ao serviço militar.
if idade < 18:
    saldo = 18 - idade
    print('Ainda não é hora de se alistar, nos vemos em {} anos.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))

# - Se é a hora de se alistar ao serviço militar. 
elif idade == 18: 
    print('Está na hora de se alistar, O país precisa de seus serviços!')

# - Se já passou do tempo do alistamento. 
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado a {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))

  
        

