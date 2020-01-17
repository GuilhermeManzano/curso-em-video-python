#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

s = float(input('Qual o salário do funcionário?: R$ '))
a = s*1.15
print('O salário do funcionário era de R$ {}, mas com o aumento de 15%, passou a ser de R$ {}'.format(s, a))