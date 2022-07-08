# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite algo aqui: ')
print(type(n))
print('Esta variável é alfanumérico? ', n.isalnum())
print('Esta variável é apenas alfabeto? ', n.isalpha())
print('Est variável foi escrito em ASCII? ', n.isascii())
print('A variável é decimal? ', n.isdecimal())
print('Esta variável é apenas de letras minusculas? ', n.islower())
print('Esta variável é apenas de números? ', n.isnumeric())
print('Esta variável pode ser exibida? ', n.isprintable())
print('Contem espaços nesta variável? ', n.isspace())
print('É um título? ', n.istitle())
print('Esta variável é escrita em letras maiusculas? ', n.isupper())

# Importante ler as dicas que o idle avisa sobre possível erros de sintaxe e como corrigir.
