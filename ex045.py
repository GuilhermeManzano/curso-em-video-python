# Crie um programa que faça o computador jogar Jokenpô (pedra, papel e tesoura) com você

from random import choice
print('O computador já fez a sua escolha, será que você consegue ganhar dele?')
print('Qual a sua escolha? \n \033[1;34;41m [ 1 ] Pedra \033[m')
print(' \033[1;32;46m [ 2 ] Papel \033[m \n \033[7;30;41m [ 3 ] Tesoura\033[m')
a = 'pedra'
b = 'papel'
c = 'tesoura'
j = int(input('Digite a opção desejada: '))
r = choice([a, b, c])
if j == 1 or j == 2 or j ==3:
    if j == 1:
        if r == a:
            print('Você escolheu pedra e o computador escolheu {}. Deu empate!'.format(a))
        elif r == b:
            print('Você escolheu pedra e o computador escolheu {}. O computador ganhou! Que pena!'.format(b))
        elif r == c:
            print('Você escolheu pedra e o computador escolheu {}. Parabéns, você ganhou!'.format(c))
    if j == 2:
        if r == a:
            print('Você escolheu papel e o computador escolheu {}. Parabéns, você ganhou!'.format(a))
        elif r == b:
            print('Você escolheu papel e o computador escolheu {}. Deu empate!'.format(b))
        elif r == c:
            print('Você escolheu papel e o computador escolheu {}. O computador ganhou! Que pena!'.format(c))
    if j == 3:
        if r == a:
            print('Você escolheu tesoura e o computador escolheu {}. O computador ganhou! Que pena!'.format(a))
        elif r == b:
            print('Você escolheu tesoura e o computador escolheu {}. Parabéns, você ganhou!'.format(b))
        elif r == c:
            print('Você escolheu tesoura e o computador escolheu {}. Deu empate!'.format(c))
else:
    print('Opção inválida, tente novamente.')
