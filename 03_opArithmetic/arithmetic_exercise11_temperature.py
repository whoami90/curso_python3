# Escreva um programa que converte uma temperatura digitada em ºC e converta para ºF. E depois para Kelvin.
# Dados: Temperatura fornecida pelo usuário
# Dados: Parâmetros : 1ºC = 33.8ºF 
# Dados extra: 1ºC = 274,15K
# O que fazer com estes dados? : Calcular e converter a temperatura fornecida pelo usuário para ºF e K.
# Restrições: usar float
# O que é esperado deste programa?: Poder exibir na tela a temperatura inserida pelo usuário em ºF e tambem em K.

temperatura = float(input('Qual é a temperatura aí onde você está? '))
far = (temperatura * 9/5) + 32
kel = (temperatura + 273.15)
print('A temperatura onde você está é {} ºC equivale a {} ºF \n ou {} K em outros países.'.format(temperatura, far, kel))
