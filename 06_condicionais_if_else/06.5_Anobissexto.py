'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto. 

'''

# Para saber se um ano é bisexto basta dividir ele por 4, não pode ser multiplo de 100 e nem de 400, se for número exato e respeitar as demais regras, é bissexto, senão não é. 
from datetime import date

ano = int(input('Digite aqui o ano que queira verificar: Coloque 0 para analisar o ano atual!: '))
if ano == 0:
    ano = date.today().year  # função qie puxa o ano atual da máquina.
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0 :  #Verificando todas as regras para ver se o ano é ou não bissexto, divisível por 4 e 400 e nao múltiplo de 100.
    print('O ano {} é Bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
