# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

from math import ceil
c = int(input('\033[0;35;m Qual é o valor da casa?: R$ \033[m'))
s = int(input('\033[7;30m Qual o salário do comprador?: R$ \033[m'))
a = int(input('\033[4;31;43m Em quantos anos você pagará a casa?: \033[m'))
p = (c/(a*12))
if s*.3 >= p:
    print('Seu empréstimo foi aprovado! Você pagará parcelas de R$ {} da casa em {} anos '.format(ceil(p), a))
else:
   print('Que pena! Parece que você não se enquadra dentro do nosso perfil e seu empréstimo foi negado.')
