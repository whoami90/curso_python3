'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valore de seu aumento. 
Para salários superiores a R$1.200,00, calcule um aumento de 10%. 
Para os salários inferiores ou iguais o aumento é de 15%. 
'''
salario = float(input('Qual é o valor de salário do funcionário? R$ '))
# Verificação se o funcionário ganha mais de R$1.200 de salário.
if salario >= 1200:
    print('O salário é de R${:.2f}, com o aumento vai para R${:.2f}'.format(salario, ((salario * 10) / 100 + salario)))
# Verificação se o funcionário ganha menos de R$1.200 de salário.
else:
    print('O salário é de R${:.2f}, com o aumento vai para R${:.2f}'.format(salario, ((salario * 15) / 100 + salario)))

