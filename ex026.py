#Faça um programa que leia uma frase pelo teclado e mostre: a) Quantas vezes aparece a letra "A"
# b) Em que posição ela aparece a primeira vez. c) Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip()
b = frase.upper()
print('A letra A aparece {} vezes na frase'.format(b.count('A')))
print('A primeira letra A aparece na posição {}'.format(b.find('A')))
print('A última letra A aparece na posição {}'.format(b.rfind('A')))
