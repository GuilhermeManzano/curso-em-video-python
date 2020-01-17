#Escreva um programa que pergunte o salário do funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

from math import ceil
s = int(input('Qual é o seu salário? R$ '))
if s > 1250:
    a = s*0.1
    print('O seu salário é de R$ {} e você receberá um aumento de R$ {}'.format(s, ceil(a)))
else:
    a = s*0.15
    print('O seu salário é de R$ {} e você receberá um aumento de R$ {}'.format(s, ceil(a)))
