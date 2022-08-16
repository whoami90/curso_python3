# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

# input
area_pin = float(input('Tamanho da área a ser pintada em m²: '))  # área a ser pintada 
area_cobe = 3 # área de cobertura 1litro = 3m²
lata = 18 # tamanho da lata de tinta em litros
preco_lata = 80  # preço da lata de tinta 
# calculos
quantidade_latas = math.ceil((area_pin / area_cobe) / lata)
valor_total = quantidade_latas * preco_lata
# output
print('Serão necessários {} latas de tinta para pintar a área definida'.format(quantidade_latas))
print('O valor total da compra é de R${:.2f}'.format(valor_total))