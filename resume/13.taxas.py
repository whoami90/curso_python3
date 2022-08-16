# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que 
# João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

peso = float(input('Insira aqui o peso do pescado: '))
excesso = peso - 50
multa = excesso * 4
if peso > 50:
 print('O pescado teve o total de {}kg'.format(peso))
 print('Excedeu o total de {} kg e o valor da multa é R${:.2f}'.format(excesso, multa))
else:
    print('Peso dentro da quantidade mínima!')
    print('Tenha um bom dia!')
    