# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com os valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for a in range(0, 3):
   for b in range(0, 3):
      matriz[a][b] = int(input(f'Digite um valor para [{a}, {b}]: '))
for a in range(0, 3):
   for b in range(0, 3):
       print(f'[{matriz[a][b]}]', end='')
   print()
