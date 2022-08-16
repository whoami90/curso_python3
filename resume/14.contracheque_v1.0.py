# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.

# Obs.: Salário Bruto - Descontos = Salário Líquido.

valor_hora = float(input('Valor hora trabalhada: R$ '))
total_horas_mes = int(input('Total de horas trabalhadas no mês: '))
salario_bruto = valor_hora * total_horas_mes
irpf = (salario_bruto * 11 / 100)
inss = (salario_bruto * 8 / 100)
sindicato = (salario_bruto * 5 / 100)
descontos = irpf + inss + sindicato
salario_liquido = salario_bruto - descontos
print('+ Salário Bruto: R$ {:.2f}'.format(salario_bruto))
print('- IR (11%): R$ {:.2f}'.format(irpf))
print('- INSS (8%): R$ {:.2f}'.format(inss))
print('- Sindicato (5%): R$ {:.2f}'.format(sindicato))
print('= Salário Líquido: R$ {:.2f}'.format(salario_liquido))
