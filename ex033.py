#Faça um programa que leia três números e mostre qual o menor e qual é o menor.

x1 = int(input('Digite o primeiro número: '))
x2 = int(input('Digite o segundo número: '))
x3 = int(input('Digite o terceiro número: '))

if x1 > x2 and x1 > x3:
    if x2 > x3:
       print('O maior número é {} e o menor número é {}'.format(x1, x3))
    else:
       print('O maior número é {} e o menor número é {}'.format(x1, x2))
else:
    if x2 > x1 and x2 > x3:
        if x1 > x3:
            print('O maior número é {} e o menor número é {}'.format(x2, x3))
        else:
            print('O maior número é {} e o menor número é {}'.format(x2, x1))
    else:
        if x2 > x1:
            print('O maior número é {} e o menor número é {}'.format(x3, x1))
        else:
            print('O maior número é {} e o menor número é {}'.format(x3, x2))
