# Crie um programa que leia o quanto uma pessoa tem na carteira e mostre quantos dólares ele pode comprar.
# Considere: US$1.00 = R$3.27

re = float(input('Quanto dinheiro você para trocar por dóláres? R$'))
dol = re / 3.27
print('Com {:.2f} reais é possível trocar por {:.2f} dólares'.format(re, dol))
