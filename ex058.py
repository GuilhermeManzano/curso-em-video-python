# Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

tent = 0
r = randint(0, 10)
n = 0
while n != r:
   print('Que pena! Você errou! Tente novamente')
   n = int(input('Pensei em um número entre 1 e 10. Qual número eu pensei?: '))
   tent += 1
print('Parabéns, você acertou! Você fez {} palpites até acertar o número que eu pensei'.format(tent))
