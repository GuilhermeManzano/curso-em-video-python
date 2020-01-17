# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math
n = float(input('Digite um número: '))
i = math.trunc(n)
print('O número {} tem a parte inteira {}'.format(n, i))
