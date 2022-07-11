'''
Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by third.
Display the answer as The answer is [answer]

'''
num1 = int(input('Insert here a first number: '))
num2 = int(input('Insert here a second number: '))
num3 = int(input('Insert here a third number: '))
answer = (num1 + num2) * num3
print('The answer this equation is {}'.format(answer))
