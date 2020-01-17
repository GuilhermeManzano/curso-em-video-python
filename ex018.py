# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do Seno, do Cosseno e a Tangente desse ângulo.

import math

a = int(input('Digite o ângulo que você deseja: '))
se = math.sin(math.radians(a))
co = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print('O ângulo de {}° tem o Seno de: {:.2f}'.format(a, se))
print('O ângulo de {}° tem o Cosseno de: {:.2f}'.format(a, co))
print('O ângulo de {}° tem a Tangente de {:.2f}'.format(a, tg))
