'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'.

-> Dados: nome de uma cidade fornecido pelo usuário.
-> Comparar o nome da cidade e comparar se a primeira palavra é santo. 
-> Não deve conter numeros, apenas string.
-> Poder exibir na tela se o nome inserido pelo usuário é ou não verdadeiro, ou seja, tem ou não a palavra santo.
-> Como farei: 
* receber o nome por input
* eliminar os espaços antes de depois da palavra, caso o usuário tenha colocado
'''

cid = str(input('Em que cidade você nasceu? ')).strip()
# input expecificando que a palavra desejada deve ser em string. O .strip() no final serve para tirar os espaços desnecessários. 
print(cid[:5].capitalize() == 'Santo')
# No print foi realizado a verificação dos dígitos da palavra santo para ver se é igual com a palavra e capitalize para colocar a primeria letra maiuscula, porem pode ser utilizado .upper() tudo maiusculo ou . lower() tudo minusculo porem para isso é necessário tambem deixar a palavra de comparação da forma desejada. 

# Como programador é importante imaginar o seguinte, quando for programar uma solução pense o usuário pode fazer alguma besteira, e ele normalmente faz. 
