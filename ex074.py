# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem dos números gerados e também indique o menor e o maior valor que estão na tupla.

import random

n = maior = menor = 0
print('Os valores sorteado foram: ', end='')
while n < 5:
    num = random.randint(0, 100)
    print(num, end=' ')
    if n == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    n += 1
print(f' \nO menor número sorteado foi: {menor}')
print(f' \nO maior número sorteado foi: {maior}')
