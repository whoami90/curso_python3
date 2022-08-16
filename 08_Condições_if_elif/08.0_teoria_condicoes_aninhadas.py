
# Teoria Condições aninhadas

'''
if
bloco1, sempre deve ser utlizado
elif
bloco2, dentro de elif pode ser usado várias vezes
else
bloco3, pode ou não ser utilizado
'''
nome = str(input('Qual é o seu nome? '))
if nome == 'Naftali':
    print('Que nome diferente!') # caso queira manter apenas esta estrutura + mais o print inferior funciona normalmente. Apenas if = Condição simples.
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')  # Com a função elif temos o que chamamos de condição aninhada
else:
    print('Seu nome é bem comum por aqui!') # If e Else = condição composta. 
print('Tenha um bom dia, {}!'.format(nome))