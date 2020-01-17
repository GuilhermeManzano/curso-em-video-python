# Faça um programa que tenha uma função que receba três parâmetros: inicio, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada. A) De 1 até 10, de 1 em 1. B) De 10 até 0, de 2 em 2. C) Uma contagem personalizada


def passos(i, f, p):
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end=' ', flush=True)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            cont -= p
        print('FIM')
    print('-=' * 20)


passos(1, 10, 1)
passos(10, 0, 2)
print('Agora é a sua vez de pesonalizar a contagem')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
passos(ini, fim, pas)
