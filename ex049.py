# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número de 1 a 9: '))
if 1 < n < 9:
  print('-' * 20)
  for c in range(0, 10, 1):
    print('{} x {:2} = {}'.format(n, c+1, n*(c+1)))
  print('-' * 20)
else:
    print('Digite um número entre 1 e 9')
