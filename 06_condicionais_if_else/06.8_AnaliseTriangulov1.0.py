'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. 
'''

from time import sleep


print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)
# Inserção dos lados do triângulo
r1 = int(input('Qual é o primeiro segmento: '))
r2 = int(input('Qual é o segundo segmento: '))
r3 = int(input('Qual é o terceiro segmento: '))
# Um pouco de charme. 
sleep(1)
print('Analisando se é possível formar um triângulo.')
sleep(1)
print('*')
sleep(1)
print('**')
sleep(1)
print('***')

# Verificando se é possivel formar um triangulo. 
# Regra matemática: Para ser possível formar um triângulo, é necessário que cada um dos segmentos seja menor que a soma do comprimento dos outros dois. 
if r1 > (r2 + r3) or r2 > (r1 + r3) or r3 > (r1 + r2):
    print('Não é posível formar um triângulo!')
else: 
    print('É possível formar um triângulo!')
