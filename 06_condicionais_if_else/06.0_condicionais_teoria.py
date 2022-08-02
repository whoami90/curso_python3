'''
Condições em Python (if... else)

Condições simples e Condições compostas

Condição
if car.left():
 block_v_
else:
 block_F_  

* Sempre que se trabalha com condicionais é importante se atentar que é necessário criar um bloco para ser executado caso a condicional seja ativada (verdadeiro) e tambem um bloco para ser executado caso o bloco verdadeiro não seja ativado. Portanto será ativado o segundo bloco (Falso).
* Uma ou outra é acionada, nunca as duas. 
'''
# Exemplo 1 

tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3: 
	print('Carro novo')
else:
	print('Carro velho')
print('--Fim--')

'''
* Dica para fazer a indentaçção corretamente, usar tab 1x ao inves de apertar space. 
* Sempre que for colocar os prints relacionados a alguma condicional é necessário utilizar a indentação. 

* No python é possível colocar uma condicional utilizando apenas 1 linha, isto é chamado de condicional simples. 

'''

# Exemplo 2 - Condições simples

tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')

# Exemplo sem else. Com estrutura simples.

nome = str(input('Qual é o seu nome? '))
if nome == 'Naftali':
	print('Seu nome é diferente!')
print('Bom dia {}!'.format(nome))     	# Desta forma também funciona dentro do Python mesmo sem o uso do else. 

# Exemplo de estrutura composta. 

nome = str(input('Qual é o seu nome? '))
if nome == 'Naftali':
	print('Seu nome é diferente!')
else:
	print('Conheço uma pessoa que também se chama {}'.format(nome))
print('Tenha um bom dia, {}!'.format(nome))

# Exemplo utilizando notas escolares: 

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2 
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0: 
	print('Aprovado!')
else: 
	print('Reprovado!')

print('Parabens!' if m >= 6 else 'Estude mais!')  # esta opção abaixo que é condição simplificada. 