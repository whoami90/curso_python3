'''
Faça um progrma que leia três números e mostre na tela qual é o maior e qual é o menor. 
'''

n1 = int(input('Digite aqui o primeiro número: '))
n2 = int(input('Digite aqui o segundo número: '))
n3 = int(input('Digite aqui o terceiro número: '))
# Verificando quem é o menor.
menor = n1  # Ao invés de fazer a comparação entre os três, usar eliminação e caso o n1 não for o menor, será substituido após a verificação.
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando quem é o maior, utilizando o mesmo procedimento de eliminação usado acima. 
maior = n3
if n3 > n1 and n3 > n2:
    maior = n3
if n2 > n1 and n2 > n3:
    maior = n2
print('O menor número é o {} e o maior número é o {}'.format(menor, maior))

