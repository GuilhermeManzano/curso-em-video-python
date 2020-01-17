#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

a = int(input('Digite um ano qualquer: '))
h1 = a % 4
h2 = a % 400
if h1 == 0 or h2 == 0:
  print('O ano {} é BISSSEXTO'.format(a))
else:
  print('O ano {} não é BISSSEXTO'.format(a))
