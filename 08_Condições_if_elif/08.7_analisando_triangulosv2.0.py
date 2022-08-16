'''
Refaça o DESAFIO 1.0 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: 
'''

# Equilátero: todos os lados iguais.
# Isóceles: dois lados iguais.
# Escaleno: todos os lados diferentes. 

from time import sleep


print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)
# Inserção dos lados do triângulo
r1 = int(input('Qual é o primeiro segmento: '))
r2 = int(input('Qual é o segundo segmento: '))
r3 = int(input('Qual é o terceiro segmento: '))
# Tipo de triangulos:
# equilátero (todos os lados iguais)
# equilatero = r1 == r2 == r3
# Isóceles (dois lados iguais)
# isoceles = r1 == r2 != 3 or r1 == r3 != r2 
# Escaleno (todos os lados diferentes)
# escaleno = r1 != r2 and r1 != r3 and r2 !=r3

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
    if r1 == r2 == r3:
        print('Este é um triângulo equilátero')
    elif r1 == r2 != 3 or r1 == r3 != r2:
        print('Este é um triângulo isóceles!')
    else: 
        print('Este é um triângulo escaleno.')
