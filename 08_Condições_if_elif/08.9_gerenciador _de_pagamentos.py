'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
 preço normal e condição de pagamento.
'''
print('{:=^40}'.format(' Lojas Arapuã '))
# Dados: 
print(' ')
preço = float(input('Qual é o valor do produto? R$ '))
print(' ')
print(''' Formas de pagamento
[ 1 ] Dinheiro a vista ou cheque
[ 2 ] A vísta no cartão 
[ 3 ] Parcelado em 2x no cartão
[ 4 ] parcelado em mais de 3x no cartão
''')
opcao = int(input('Qual a forma de pagamento escolida? '))

# A vista dinheiro / cheque: 10% de desconto
if opcao == 1:
    total = preço - (preço * 10 / 100)
# Á vista no cartão: 5% de desconto
elif opcao == 2:
    total = preço - (preço * 10 / 100)
# Em até 2x no cartão: preço normal
elif opcao == 3: 
  total = preço
  parcela = total / 2
  print('Sua parcela será de 2x vezes de R${:.2f}, sem juros'.format(parcela))
# 3x ou mais no cartão: 20% de juros. 
elif opcao == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Qual o total de parcelas desejado? '))
    parcela = total / totparc
    print('Sua parcela será {} vezes de R${:.2f}, com juros!'.format(totparc, parcela))
else:
    total = 0
    print('\033[31mOPÇÃO INVALIDA!\033[m Tente novamente!')   # Opção para escolhas erradas

print('Sua compra de R${:.2f} com a forma de pagamento escolhida será de R${:.2f} no final'.format(preço, total))

