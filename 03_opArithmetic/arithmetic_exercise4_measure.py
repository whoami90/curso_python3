# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

'''
Dados: número em metros fornecido pelo usuário
O que fazer com estes dados: converter o número fornecido pelo usuário em centímetros e milímetros.
Restrições: Deve ser utiizados números inteiros.
O que se espera deste programa: Exibir na tela o número inserido pelo usuário e convertido para mas metricas centímetros e milímetros. 
{} metros equivale a {} centímetros e {} milímetros


1 metro = 100 centímetros == 1/100
1 metro = 1000 milímetros == 1/1000

Escala: 
1 metro: 
Km = 100  hm = 100 dam = 10 m = 1 dm = 10 cm =100 mm = 1000

'''
num = int(input('Digite aqui uma distancia em metros: '))
m1 = num * 100
m2 = num * 1000
print('{} metros equivale a {} centímetros e {} milímetros'.format(num, m1, m2))

n = int(input('Digite aqui uma distancia em metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print('A distância {} m, equivale a {} km, {} hm, {} dam, {} dm, {} cm e {} mm'.format(n, km, hm, dam, dm, cm, mm))
