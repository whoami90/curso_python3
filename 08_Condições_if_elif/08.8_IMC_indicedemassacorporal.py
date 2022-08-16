'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: 

->  Instruções: 
IMC = peso / altura²

'''
# Dados:
peso = float(input('Qual é o seu peso atual? '))
altura = float(input('Qual é a sua altura? '))
# Calculo:
imc = peso / (altura ** 2)
print('O seu imc é {:.1f}'.format(imc))
# Abaixo de 18.5: Abaixo do peso
if imc <= 18.5:
    print('Você está abaixo do peso!')
# Entre 18.5 e 25: Peso ideal
elif imc <= 25:
    print('Você está em um peso ideal')
# Entre 25 e 30: Sobrepeso
elif imc <= 30:
    print('Você está em sobrepeso.')
# Entre 30 e 40: Obesidade
elif imc <= 40:
    print('Vocé está em um quadro de obesidade.')
# Acima de 40: Obesidade mórbida
else:
    print('Você está em um quadro de obesidade mórbida.')
