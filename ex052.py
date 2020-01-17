# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

div = 0
n = int(input('Digite um número: '))
for c in range(1, n+1):
    if n % c == 0:
      div = div + 1
if div == 2:
  print('O número escolhido é primo')
else:
  print('O número escolhido NÃO é primo')
