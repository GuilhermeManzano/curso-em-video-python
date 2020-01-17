# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time
for c in range(10, -1, -1):
  print('Contagem regressiva: {}'.format(c))
  time.sleep(1)
print('Queima de Fogos')
