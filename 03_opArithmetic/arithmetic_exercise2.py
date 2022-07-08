# Crie um algorítimo que leia um número e mostre o seu dobro, seu triplo e sua raiz quadrada.

'''
Dados: número fornecido pelo usuário, seu dobro, triplo, sua raiz quadrada
O que fazer com estes dados: Exibir na tela o dobro, triplo e a raiz quadrada do número inserido pelo usuário.
Restrições: Deve ser inserido um número inteiro.
O que se espera deste problema: Exibir na tela o dobro, o triplo e a raiz quadrada do número de forma amigável.
'''

num = int(input('Digite aqui um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(
    num, dobro, triplo, raiz))

# Para diminuir o tamanho das casas decimais basta colocar {:.'numeros de casas decimaisf} -> f = float
# Outra possibilidade é fazer tudo dentro do print direto.

n = int(input('Digite um número: '))
print('Analisando o número {} o dobro é {}, o triplo é {} e a sua raiz quadrada é {:.2f}'.format(n, (n*2), (n*3), (n**(1/2))))
