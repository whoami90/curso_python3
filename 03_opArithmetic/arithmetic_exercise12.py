# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. 

'''
Dados: Quilometragem rodada pelo usuário. 
Dados: R$60 p/dia
Dados: R$0,15 p/km rodado
O que fazer com estes dados: Calcular o quanto o usuário precisará pagar pelo aluguel do carro. 
Restrições: O gasto dia é fixo e a quilometragem é variável de acordo com o quanto o usuário rodou com o carro.
O que é esperado do programa: Poder exibir na tela o quanto o usuário deverá pagar pela utilização do carro.
'''
dias = float(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilometros você rodou com o carro em km? '))
valor_dias = (dias * 60)
valor_rodado = (km * 0.15)
valor_total = valor_dias + valor_rodado
print('O carro foi alugado por {} dias e rodou {}km, portanto o valor do aluguel é de R${:.2f}'.format(dias, km, valor_total))

