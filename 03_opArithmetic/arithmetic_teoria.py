'''
Na programação estes são os operadores aritméticos: 

+ adição  -- 5 + 2 == 7
- subtração -- 5 - 2 == 3 
* Multiplicação -- 5 * 2 == 10 
/ divisão -- 5 / 2 == 2.5
** Potência -- 5 ** 2 == 5² == 25
// Divisão inteira -- 5 // 2 == 2  (apenas a divisão inteira, sem o resto)
% resto da divisão -- 5 % 2 == 1 (Apenas o resto tem o resultado da divisão inteira)

Para problemas aritméticos, somente poderá ser utilizado números e variáveis que contenham números, strings não é possivel utilizar. 
No python == significa igual, = significa recebe. (Outras linguagens tambem usam esta sintaxe.)

Ordem de Precedencia dos operadores: 

1. ()  # Na matemática tem () {} [], porem no Python apenas (), os outros possuem outras funções dentro da matemática.
2. **
3. * / // %
4. + - 

 Caso dentro da operação possua vários elementos diferentes siga a ordem de procedencia, caso apenas possua a da 3ª casa, faça na ordem que o problema pede.
-> Um programa funcionar, não significa que está certo. Por causa dos operadores. 
-> O python não dar erros não significa que o programa está certo, significa que não possui erro de sintaxe. Mas poder ter erro de calculo. 
Exemplo:

5 + 3 * 2 == 11
3 * 5 + 4 ** 2 == 31
3 * (5 + 4) ** 2 == 243
5 ** 3 == 125
19 // 2 == 9 
19 / 2 == 9.5
18 % 2 == 0

Potência também pode ser realizado de outra forma: 

4 ** 3 == 64  <- Operador de potência
pow(4,3) == 64  <- Função interna de potência

Raiz quadrada:
81 ** (1/2) == 9  
25 ** (1/2) == 5
# Calcular a raiz quadrada de um número é o mesmo que calcular sua potência por 1/2

Raiz cúbica:

127 ** (1/3) == 5.026

No Python ele não faz operações aritméticas com strings, ele concatena, porém tem algumas funcionalidades interessantes com isso. 

'Oi' + 'Oi' = OiOi
'Oi' * 5 = OiOiOiOiOi
'=' * 20 =  ====================

'''
nome = input('Digite aqui o seu nome: ')
print('Prazer em te conhecer {},seja bem vindo!'.format(nome))
print('Pazer em te conhecer {:20}, seja bem vindo!'.format(nome))
print('Prazer em te conhecer {:>20}, seja bem vindo!'.format(nome))
print('Prazer em te conhecer {:<20}, seja bem vindo!'.format(nome))
print('Prazer em te conhecer {:^20}, seja bem vindo!'.format(nome))
print('Prazer em te conhecer {:=^20}, seja bem vindo!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}'.format(s))
print('A multiplicação vale {}'.format(m))
print('A Divisão é {}'.format(d))
print('A divisão inteira é {}'.format(di))
print('A exponênciação é {}'.format(e))

'''
Caso queira melhorar a formatação acima pode se usar todas as variáveis uma única linha também. 

'''
print('A soma vale {}, a multiplicação vale {}, a divisão vale {}'.format(s, m, d))
print('A divisão inteira vale {} e a expônenciação vale {}'.format(di, e))

'''
Com o print acima, a linha foi quebrada, pois foi utilizado dois prints.
Caso queira que seja exibido em apenas 1 linha também é possível. 
para isso usa-se end=''
'''
print('A soma vale {}, a multiplicação vale {}, a divisão vale{}'.format(s, m, d), end='')
print('A divisão inteira vale {} e a expônenciação vale {}'.format(di, e))

'''
Para quebrar uma linha em pontos expecíficos, basta utilizar a \n nos pontos onde queira quebrar a linha.

'''
