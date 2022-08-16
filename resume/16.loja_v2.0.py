# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida 
# em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math

# área a ser pintada 
area = float(input('Qual o tamanho da área a ser pintada em m²: '))

# cobertura da tinta
uso_1l = 6

# latas 
lata = 18
galao = 3.6

# valor das latas
valor_lata = 80
valor_galao = 25

# quantidade de litros de tinta a ser utilizada
quantidade_utilizada = (area / uso_1l)

# condicional para definir se será utilizado latas ou galão
if quantidade_utilizada > 0 and quantidade_utilizada <= 3.6:
    print('A quantidade de tinta necessária para pintar a área desejada é de {:.2f}'.format(quantidade_utilizada))
    print('Para esta quantidade indicamos o galão de 3,6 litros, ele está custando R${:.2f}'.format(valor_galao))
elif quantidade_utilizada > 3.6 and quantidade_utilizada < 18:
    print('A quantidade de tinta necessária para pintar a área desejada é de {:.2f}'.format(quantidade_utilizada))
    print('Para esta quantidade será necessário {} galoes de 3.6L, o valor é R$ {:.2f}'.format((quantidade_utilizada / 3.6), 25 * (quantidade_utilizada / 3.6)))
