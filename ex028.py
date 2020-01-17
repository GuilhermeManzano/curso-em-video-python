#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import choice

n = int(input('Pensei em um número entre 0 e 5. Qual número eu pensei?: '))
r = choice([1, 2, 3, 4, 5])
if n == r:
   print('Parabéns! Você acertou!')
else:
   print('Que pena! Você errou')
