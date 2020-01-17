# Crie um programa que mostre na tela todos os números pares que estão no invervalo entre 1 e 50.

for c in range(0, 51, +1):
    p = c%2
    if p == 0:
        print('O número {} é PAR'.format(c))
print('Fim do Programa')