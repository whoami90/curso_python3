'''
Teoria cores no terminal: 

Existem várias formas de colocar cores dentro do terminal, pode ser por bibliotecas ou também  pode ser ultilizado ANSI (escape sequence)

código ansi para cores: 
\033[m

os códigos para as cores devem ser inseridos entre [ e a letra m 

serão utilizados até 3 códigos separados por ponto e vírgula ';' que indicarão: style (fonte) ; text (texto) ; back (background cor do fundo)

*** Pode colocar em qualquer ordem, pois o Python sabe diferenciar a codificação numérica de cada um dos códigos identifcando cada uma delas. 

style: 0 (none), 1 (bold), 4 (underline), 7 (negative)  -- existem outros porem até o momento é o que funciona melhor no terminal python.
text: 30 w , 31 r , 32 g , 33y , 34 b, 35 p, 36 l.b , 37 s    -- cores 
back: 40 w , 41 r , 42 g , 43y , 44 b, 45 p, 46 l.b , 47 s

exemplo: 

\033[0;33;44m
'''
# Exibir na tela a palavra teste com letra branca e fundo vermelho.
from xml.dom import ValidationErr


print('\033[0;30;41mTeste')
# Exibir na tela a palavra teste com letra amarela sublinhada e fundo azul claro.
print('\033[4;33;44mTeste')
# Exibir na tela a palavra teste em negrito com letra rosa e fundo amarelo.
print('\033[1;35;43mTeste')
# Exibir na tela a palavra teste com letra branca e fundo verde.
print('\033[30:42mTeste')
# Teste com letra branca e fundo preto - é o padrão do terminal, tecnicamente esta opção tira todas as formatações.
print('\033[mTeste')
# Exibir na tela a palavra teste com letra preta e fundo branco. 
print('\033[7;30mTeste')

# Prática
print('\033[4;1;33;44mHello World\033[m')  # No final do código foi inserido a função que retorna o padrão do terminal, desta forma apenas o que estiver dentro das '' será alterado.

a = 3
b = 5
print('Os valores são \033[32m{} e \033[31m{}\033[m'.format(3, 5))

# Alem da opção de usar o ANSI para cores, tem a opção tambem de trabalhar com a função colorize

# Outra forma de colocar as cores: 
nome  = 'Luke'
print('{}{}{}, eu sou seu pai!'.format('\033[1;31;40m' , nome , '\033[m'))

# Mais uma forma de trabalhar com cores: 
nome = 'Naftali'
cores = {'limpa':'\033[m' ,
          'azul': '\033[34m' ,
          'amarelo': '\033[33m' ,
           'pretoebranco': '\033[7;30m'}
print('Olá {}{}{}, tudo bem!'.format(cores['azul'] , nome , cores['limpa']))

# Esta última forma é bastante útil caso queira colocar vários itens coloridos pelo código e não queira digitar o código de cores o tempo todo, basta criar a paleta de cores e pronto. 


