# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

h = float(input('Digite aqui sua altura: '))
print(''' Digite o Gênero
1 - homem
2 - mulher
''')
genero = int(input('Qual o genero escolhido: '))
peso_homem = float((72.7 * h) - 58)
peso_mulher = float((62.1 * h) - 44.7)

if genero == 1:
    print('Seu peso ideal é {:.2f}'.format(peso_homem))
elif genero == 2:
    print('Seu peso ideal é {:.2f}'.format(peso_mulher))
else:
    print('Opção incorreta!')