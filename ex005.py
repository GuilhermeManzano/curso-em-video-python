#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.

n = int(input('Digite um número: '))
s = n + 1
a = n - 1
print('O número escolhido é {}, o seu sucessor é {} e o seu antecessor é {}.'.format(n, s, a))