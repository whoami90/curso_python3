'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adsjacente de um triângulo retângulo, 
calcule e mostre o comprimento da hipotenusa. 

a² = b²+c²
'''
# esta é a forma matemática de resolver este problema sem importação. 
'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adsjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
# hipotenusa é a raiz quadrada da soma catetos ao quadrado. 
print('A hipotenusa irá medir {:.2f}'.format(hi))
'''
# Esta é a forma com importação: 
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hi = math.hypot(co, ca)
# A função hypot é o calculo da hipotenusa. 
print('A hipotenusa irá medir {:.2f}'.format(hi))
