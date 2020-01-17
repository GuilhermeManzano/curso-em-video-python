# Crie um programa que leia o nome completo de uma pessoa e mostre: 1. O nome com todas as letras maísculas e minúsculas.
# 2. Quantas letras no total (sem considerar os espaços) 3. Quantas letras tem o primeiro nome.

n = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(n.upper()))
print('Seu nome em minúsculas é {}'.format(n.lower()))
print('Seu nome tem ao todo {} letras'.format(len(n) - n.count(' '))) #A função len conta quantas letras tem sem espaços laterais e subtrai pelos espaços INTERNOS no nome
separa = n.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
