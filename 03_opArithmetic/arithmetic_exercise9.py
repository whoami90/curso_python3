# Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario_atual = float(input('Salário atual do funcionário: '))
novo_salario = salario_atual + ((salario_atual * 15) / 100)
print('O salário do funcionário era R${:.2f} e após o aumento de 15% ele passará a ganhar ganhar R${:.2f} de salário. '.format(
    salario_atual, novo_salario))
