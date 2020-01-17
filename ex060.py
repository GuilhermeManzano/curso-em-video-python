# Faça um programa que leia um número qualquer e mostre seu fatorial.

n = int(input('Digite um número: '))
fat = n
f = 1
print('Calculando o fatorial de {}!'.format(n))
while fat != 0:
    print('{} '.format(fat), end='')
    print(' x ' if fat > 1 else '= ', end='')
    f = f*fat
    fat -= 1
print(f)


