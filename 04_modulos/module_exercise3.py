'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente deste ângulo.

Fómulas Sen, Cos, Tan: 
seno = cateto oposto / hipotenusa = 
cosseno = cateto adsjacente / hipotenusa = 
tangente = cateto oposto / cateto adsjacente = 

'''

import math

angulo = float(input('Digite aqui o ângulo que deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))

# O programa acima pode ser simplificado da seguinte maneira: somente foram utilizados sen, cos e tan basta importar apenas estas funções ao invés de toda a biblioteca.
# exemplo: from math import sen, cos, tan 
# Uma vez feito isso é necessário tirar todas as referencias dentro do código (remover o math.)
