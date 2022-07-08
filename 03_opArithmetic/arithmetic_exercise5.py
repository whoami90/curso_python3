# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

'''
Dados: número fornecido pelo usuário
O que fazer com estes dados: Criar uma tabuada + - * / de 0 a 10 
Quais as restrições deste programa: Deve ser utilizado números inteiros
O que se espera deste programa: Poder exibir na tela a tabuada de um número. 

'''
num = int(input('Digite um número: '))

# Tabuada de adição

a1 = num + 1
a2 = num + 2
a3 = num + 3
a4 = num + 4
a5 = num + 5
a6 = num + 6
a7 = num + 7 
a8 = num + 8
a9 = num + 9
a0 = num + 10

# Tabuada de subtração

s1 = num - 1
s2 = num - 2
s3 = num - 3
s4 = num - 4
s5 = num - 5
s6 = num - 6
s7 = num - 7 
s8 = num - 8
s9 = num - 9 
s0 = num - 10

# Tabuada de multiplicação

m1 = num * 1
m2 = num * 2
m3 = num * 3
m4 = num * 4
m5 = num * 5
m6 = num * 6
m7 = num * 7
m8 = num * 8 
m9 = num * 9 
m0 = num * 10

# Tabuada de Divisão 

d1 = num / 1
d2 = num / 2
d3 = num / 3
d4 = num / 4
d5 = num / 5
d6 = num / 6
d7 = num / 7
d8 = num / 8 
d9 = num / 9 
d0 = num / 10 

print('Tabuada de adição')
print('')
print(' {}+1={} {}+2={} {}+3={} {}+4={} {}+5={} \n {}+6={} {}+7={} {}+8={} {}+9={} {}+10={}'.format(num, a1, num, a2, num, a3, num, a4, num, a5, num, a6, num, a7, num, a8, num, a9, num, a0))
print('')
print('Tabuada de subtração')
print('')
print(' {}-1={} {}-2={} {}-3={} {}-4={} {}-5={} \n {}-6={} {}-7={} {}-8={} {}-9={} {}-10={}'.format(num, s1, num, s2, num, s3, num, s4, num, s5, num, s6, num, s7, num, s8, num, s9, num, s0))
print('')
print('Tabuada de multiplicação')
print('')
print(' {}*1={} {}*2={} {}*3={} {}*4={} {}*5={} \n {}*6={} {}*7={} {}*8={} {}*9={} {}*10={}'.format(num, m1, num, m2, num, m3, num, m4, num, m5, num, m6, num, m7, num, m8, num, m9, num, m0))
print('')
print('Tabuada de divisão')
print('')
print(' {}/1={} {}/2={} {}/3={} {}/4={} {}/5={} \n {}/6={} {}/7={} {}/8={} {}/9={:.2f} {}/10={}'.format(num, d1, num, d2, num, d3, num, d4, num, d5, num, d6, num, d7, num, d8, num, d9, num, d0))
print('')