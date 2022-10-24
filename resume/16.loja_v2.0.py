# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida 
# em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

# input
area = float(input('Digite aqui a área a ser pintada em m²: ')) # total da área em m² a ser pintada. 
area_pin = 6  # cada litro cobre 6m² de área. 
lata = 18
galao = 3.6
lata_valor = 80
galao_valor = 25
total_tinta_a_usar = (area / area_pin) +  (area / area_pin * (10/100)) # Foi acrescentado 10% de folga no total de tinta utilizado.
galoes = math.ceil(total_tinta_a_usar / 3.6)
latas_utilizadas = int(total_tinta_a_usar / 18) # para chegar ao valor de quantas latas de 18L são necessárias para pintar a área eliminando o resto.
galoes_utilizados = ((((total_tinta_a_usar % 18) / 10) * 18) / 3.6) # para chegar ao valor de quantos galões de 3.6L são necessários para pintar a área, eliminando o resto.


# condicionais e output 
if total_tinta_a_usar < 18:
    print('Para a área de {}m², recomendamos o galão de 3.6 litros, é a quantidade adequada para que não deixa desperdícios.'.format(area))
    if galao == 1:
        print('Será necessário apenas 1 galão para pintar a área desejada.')
        print('O total da compra é de R${:.2f}'.format(galao_valor))
    elif galao > 1:
        print('Serão necessários {} galões para pintar a área desejada.'.format(int(galoes)))
        print('O total da compra é de R${:.2f}'.format(galoes * 25))

elif total_tinta_a_usar == 18:
    print('Para a área de {}m², recomendamos a lata de 18 litros, é a quantidade adequada e que não deixa desperdícios')
    print('Será necessário apenas 1 lata de 18 litros para pintar a área desejada.')
    print('O total da compra é de R${:.2f}'.format(lata_valor))

elif total_tinta_a_usar > 18:
    if lata == 1:
        if galao == 1:
            print('Para a área de {}m², é necessário {} lata de 18L e {} galão de 3.6L.'.format(area, latas_utilizadas, galoes_utilizados))
            print('O valor da compra é de {:.2f}'.format((latas_utilizadas * lata_valor) + (galoes_utilizados * galao_valor)))
        elif galao > 1:
            print('Para a área de {}m², será necessário {} lata de 18L e {} galões de 3.6L.'.format(area, latas_utilizadas, galoes_utilizados))
            print('O valor da compra é de {:.2f}'.format((latas_utilizadas * lata_valor) + (galoes_utilizados * galao_valor)))
    elif lata > 1:
        if galao == 1:
            print('Para a área de {}m², será necessário {} latas de 18L e {} galão de 3.6L. '.format(area, latas_utilizadas, galoes_utilizados))
            print('O valor da compra é de {:.2f}'.format((latas_utilizadas * lata_valor) + (galoes_utilizados * galao_valor)))
        elif galao > 1:
            print('Para a área de {}m², será necessário {} latas de 18L e {} galões de 3.6L.'.format(area, latas_utilizadas, galoes_utilizados))
            print('O valor da compra é de {:.2f}'.format((latas_utilizadas * lata_valor) + (galoes_utilizados * galao_valor)))
   
else:
    print('Error!')

