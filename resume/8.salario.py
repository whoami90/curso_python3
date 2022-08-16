# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

money = float(input('Quanto ganha por hora? '))
hora = int(input('Total de horas trabalhadas este mês? '))
total = money * hora
print('O salário a receber este mês é R${:.2f}'.format(total))
