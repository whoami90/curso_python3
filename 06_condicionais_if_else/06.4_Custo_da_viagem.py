'''
Desenvolva um programa que pergunte a distância de uma viagem em km. 
Calcule o preço da passagem, cobrando R$0,50 por km e R$0,45 para viagens mais longas. 

'''

distancia = float(input('Qual a distância a ser percorrida em km? '))
if distancia <= 200:
    print('Sua viagem é curta! Para a distancia de {:.1f} km total da viagem é de R${:.2f}'.format(distancia, (distancia * 0.50)))
else:
    print('Sua viagem é longa! Para a distancia de {:.1f} km, o valor da viagem é de R${:.2f}'.format(distancia, (distancia * 0.45)))

   