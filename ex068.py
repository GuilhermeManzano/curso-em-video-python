# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0
while True:
    n = int(input('Digite um valor: '))
    c = randint(1, 10)
    tot = n + c
    pi = ' '
    r = (c + n) % 2
    while pi not in 'PpIi':
        pi = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {n} e o computador jogou {c}. Total de {tot}')
    print('DEU PAR' if tot % 2 == 0 else 'DEU ÍMPAR')
    if pi == 'P':
        print(f'Você jogou {n} e o computador jogou {c}. O resultado deu PAR')
        if tot % 2 == 0:
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif pi == 'I':
        if tot % 2 == 1:
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
