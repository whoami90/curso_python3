# Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. 

precoatual = float(input('Digite aqui o valor atual do produto: R$'))
com_desconto = precoatual - ((precoatual * 5) / 100) 
print('O preço deste produto com desconto de 5% é: R${:.2f} '.format(com_desconto))
