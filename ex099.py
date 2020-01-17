# Faça um programa que tenha uma função() chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que anaisar todos os valores e dizer qual deles é maior.

def maior(*num):
    maior = cont = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for x in num:
        print(f'{x} ', end='', flush=True)
        if cont == 0:
            maior = x
        else:
            if x > maior:
                maior = x
        cont += 1
    print(f'Foram informados {len(num)} valores ao todos.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
