'''
Crie um programa que leia duas notas de um aluno e calcule sua nédia, mostrando uma mensagem no final de acordo com a média atingida: 
'''
# dados 
nota1 = float(input('Primeira nota '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

# Média abaixo de 5.0: Reprovado
if media < 5:
    print('\033[31mReprovado!\033[m Sua média foi {}'.format(media))
# Média entre 5.0 e 6.9: Recuperação
elif media >= 5 and media <= 6.9:
    print('\033[33mEstá em recuperação!\033[m Sua média foi {}'.format(media))
# Média 7.0 ou superior: Aprovado
else:
    print('\033[32mAprovado!\033[m Sua média foi {}'.format(media))