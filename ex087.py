# Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = scol = maior = 0
for a in range(0, 3):
   for b in range(0, 3):
       matriz[a][b] = int(input(f'Digite um valor para [{a}, {b}]: '))
for a in range(0, 3):
   for b in range(0, 3):
       print(f'[{matriz[a][b]}]', end='')
       if matriz[a][b] % 2 == 0:
           soma += matriz[a][b]
   print()
print('*='*30)
print(f'A soma dos valores pares é: {soma}')
for a in range(0, 3):
    scol += matriz[a][2]
print(f'A soma dos valores da terceira coluna é: {scol}')
for b in range(0, 3):
    if b == 0:
        maior = matriz[1][0]
    else:
        if matriz[1][b] > maior:
            maior = matriz[1][b]
print(f'O maior valor da segunda coluna é: {maior}')
