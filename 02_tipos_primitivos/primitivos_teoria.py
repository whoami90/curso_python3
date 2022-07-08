'''
Como funcionam os tipos primitivos no Python e as peculiaridades do int(), float(), bool(), str().

n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
s = n1 + n2
print('A soma entre {} e {} é {}'.format(n1, n2, s))
# A operação acima não funciona, pois está usando o tipo primitivo errado. 
# para corrigir é necessário informar o tipo primitivo: 

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))


No Python os 4 tipos primitivos mais utilizados são: 

int - números inteiros = 7, -4, 0, 9875 
float - números flutuantes = 4.5, 0.075, 7.0, -15.223, pi  # no Brasil os valores são separados por virgula, mas no padrão internacional usa-se ponto. 
bool - booleanos = True, False
str - string = 'Olá', '7.5', '' -> string vazia

n = str(input('Digite algo: ')) ou n = input('Digite algo: ') = guarda uma informação do tipo string
n = float(input('Digite algo: ')) = guarda informação do tipo float
n = bool(input('Digite algo: ')) = guarda valores booleanos

caso se esqueça e queira saber qual é o tipo primitivo que está utilizando, basta utilizar o seguinte comando: 
print(type(variavel))

para se testar valores basta utilizar a seguinte sintaxe: 
n = input('Digite algo: ')
print(n.isnumeric())

= Com isso será gerado um resultado booleano onde é verificado se o valor inserido na variável é compatível com o que é pedido. 




'''
