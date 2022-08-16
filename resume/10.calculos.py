# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo.
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))

# (X * 2) * (Y / 2)
resposta1 = int((n1 * 2) * (n2 / 2))
print('\n a) o produto do dobro do primeiro com metade do segundo. \n')
print('A resposta é: {}'.format(resposta1))
# (X * 3) + Z
resposta2 = int((n1 * 3) + n3)
print('\n b) A soma do triplo do primeiro com o terceiro. \n')
print('A resposta é: {}'.format(resposta2))
# (z)³
resposta3 = int(n3 ** 3)
print('\n c) o terceiro elevado ao cubo.\n')
print('A resposta é {}'.format(resposta3))