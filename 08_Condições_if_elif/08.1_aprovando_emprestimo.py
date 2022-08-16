'''
Esscreva um programa que para aprovar o emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, 
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''

# Dados
salario = float(input('Qual o salário do cliente? R$ ' ))
valor_casa = float(input('Qual é o valor da casa a ser comprada? R$ '))
anos = int(input('Quantos anos de financiamento: '))
prestacao = valor_casa / (anos * 12)

# Restrição 
minimo = (salario * 30 / 100)

# Condição 
print('O valor das prestações foi R${:.2f} e 30% do seu salario é de R${:.2f}'.format(valor_casa / anos / 12, minimo))
if prestacao <= minimo:
    print('\033[1;32m EMPRESTIMO AUTORIZADO!\033[m O  empréstimo é de R${:.2f} na prestação de R${:.2f} por {} meses'.format(valor_casa, prestacao, (anos * 12)))
else:
    print('\033[1;31m EMPRESTIMO NEGADO!\033[m O valor das prestações excede o máximo de 30% da sua renda!')


