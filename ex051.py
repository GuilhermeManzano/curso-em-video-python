# Desenvolva um programa que elia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

n = int(input('Digite o primeiro termo de um PA: '))
r = int(input('Digite a razão da PA: '))
x = n + r*10
for n in range(n, x, r):
    print('{}'.format(n), end='-> ')
print('Acabou!')
