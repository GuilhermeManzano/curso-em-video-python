# Faça um programa que tenha uma lista chamada números e duas funçoes chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteaos pela função anterior.


from random import randint
numeros = list()


def sorteio():
    for cont in range(0, 5):
        num = randint(0, 100)
        numeros.append(num)
    print(f'Sorteando 5 valores da lista: {numeros} PRONTO!')


def somapar():
    somapareal = 0
    for c in numeros:
        if c % 2 == 0:
            somapareal += c
    print(f'A soma entre os numeros da lista {numeros} é {somapareal}')


sorteio()
somapar()
