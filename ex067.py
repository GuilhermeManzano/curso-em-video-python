# Faça um programa que mostre a tabuada de vários numeros, um de cada vez, para cada valor digitado pelo usuario. O programa será interrompido quando o numero soliticato for negativo.

while True:
    n = int(input('Quer ver a tabuada de qual número?: '))
    if n < 0:
        break
    else:
        if 1 < n < 9:
           print('-' * 20)
        for c in range(0, 10, 1):
           print('{} x {:2} = {}'.format(n, c+1, n*(c+1)))
           print('-' * 20)
print('TABUADA ENCERRADA. Volte Sempre.')
