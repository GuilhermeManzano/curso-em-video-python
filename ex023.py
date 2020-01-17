#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = int(input('Digite um número de 0 a 9999: '))
num = str(n)
separa = num.split()
print('unidade:{} dezena:{} centena:{} milhar:{}'.format(num[0], num[1], num[2], num[3]))
