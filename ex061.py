# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando estrutura while.

n = int(input('Digite o primeiro termo de um PA: '))
r = int(input('Digite a razão da PA: '))
pa = n
v = 0
print('Calculando a PA de {}'.format(n))
while v < 10:
    print('{}'.format(pa), end=' -> ')
    v += 1
    pa = n + r * v
print('Acabou!')
