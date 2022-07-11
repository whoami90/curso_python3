'''
O que são módulos? 
Também chamados de bibliotecas, são complementos para a linguagem de programação. 

O Python por exemplo é um programa muito leve e rápido, e isso só é possível por que em sua forma nativa apenas processa informações básicas. 
Para processar outras coisas, é necessário importar bibliotecas. Desta forma somente será utilizado ferramentas que são realmente necessárias. 
=======================================================================

Imaginando o corpo humano como um programa: 
Necessitamos de algumas coisas para poder sobreviver, estas coisas não vem com a gente, é preciso adicionar ao corpo. 
por exemplo: 

bebida = [chá, café, água,]
comida = [arroz, bife, ovo]
açucar = [cookies, pudim sorvete]

neste caso eu queira importar a coleção bebida basta: 

import bebida = [chá, café, água,]

* porem, será importada toda a biblioteca de bebidas. 

* Para fazer um importação de um item expecífico basta utilizar: 

from bebida import [água]
=======================================================================
Bibliotecas padrão do Python: 

math (Matemática) = operadores básicos por padrão
dentro da bilioteca tem as funções que vão alem de operadores básicos. 

ceil = arredonda um número para cima
floor = arredonda um número para baixo
trunc = trunca um número ou seja elimina os números depois do . no decimal
pow = potência
sqrt = raiz quadrada
factorial = fatorial

* Porém se usar import math irá importar tudo dentro da biblioteca muita coisa que não vem de padrão. 
* Caso queira utilizar uma função exata na matemática como apenas a raiz quadrada: from math import sqrt
* Tambem é possível importar mais de uma funcionalidade: from math import sqrt, pow
* Sem importar uma biblioteca as opções de manipulação de strings e dados fica muito restrita.
'''
# Importando todas as funções.
'''
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é {:.2f}'.format(num, raiz))
print('A raiz quadrada de {} é {}'.format(
    num, math.ceil(raiz)))  # Arredonda para cima
print('A raiz quadrada de {} é {:.2f}'.format(
    num, math.floor(raiz)))  # Arredonda para baixo

'''
# Importando funções expecíficas:

'''
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada do {} é {}'.format(num, floor(raiz)))

# importando diretamente a função, não é necessário utilizar o biblioteca.função quando for utiliza-lo. pode chamar a função direto.

# Onde encontrar bibliotecas para trabalhar com o Python?
# No site oficial do Python.org > verifique e selecione qual versão está usando > abrirá uma página com uma lista de bibliotecas, com todas as funcionalidades e exemplos de como utilizar.

# Exemplo biblioteca Random. (aleatório)

import random

num = random.random()
print(num)
# No exemplo acima do random ele cria um número float aleatório entre 0 e 1, mas é possível melhorar isto.

# Utilizando desta forma é possível chamar um número inteiro de 1 a 10
num = random.randint(1, 10)
print(num)
# Com a função acima é posssível é possível gerar números aleatórios dentro de uma cadeia de números. ex (1, 10)
# Para ter acesso a lista de bibliotecas padrão basta digitar: import + ctrl space, caso alguma biblioteca ja tenha sido adicionada no inicio do programa, somente aparecerá as funções.

# indo além das bibliotecas que podem ser importadas, em  python.org > pypi.org - tem milhares de módulos para importar separadamente. 

# Exemplo para uso: biblioteca Emoji


import Emoji
print(emoji.emojize("Hello World :thumbs_up:"))
print(emoji.demojize("Hello World :thumbs_up: "))
# Para exibir um emoji junto de uma mensagem, basta utilizar a sintaxe acima. mensagem e o código do emoji entre '' e  use_aliases=True
# Pode se utilizar uma página para verificar os códigos de emojis para poder utilizar, infelizmente o windows é bem atrasado na questão dos emojis, pois alguns podem exibir mensagem de erro e não aparecer. 
# Várias importações depois e nada, depois tentar esse passo novamente no Linux para ver se consigo ter sucesso. 

Depois que corrigir estes erros ou migrar para o Linux voltar na aula módulo #8 apartir de 18min
'''
#import emoji
#print(emoji.emojize(Hello World :thumbs_up:))

# Mesmo instalando ima máquina virtual o módulo emoji não funciona - não vou insistir. 

