# Faça um programa que leia a largura e a altura de uma parede, calcule a sua área e a quantidade de tinta necessária para pintá-la.
# Considerando que cada litro de tinta pinta uma área de 2m². 

alt = float(input('Qual a altura da parede? '))
lar = float(input('Qual a largura da parede? '))
area = alt * lar
tinta = area / 2
print('Sua parede tem a dimensão de {}m x {}m e sua área é de {:.2f}m². \n Para pintar esta parede você precisará de {:.1f}l de tinta.'.format(alt, lar, area, tinta))
