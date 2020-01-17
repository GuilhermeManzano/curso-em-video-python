# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: - O primeiro valor é maior. - O segundo valor é maior. - Não existe valor maior, os dois são iguais.

n = int(input('\033[7;35;42m Digite um número: \033[m'))
n2 = int(input('\033[1;31;43m Digite outro número: \033[m'))
if n > n2:
    print('O primeiro valor é maior')
elif n < n2:
    print('O segundo valor é maior')
else:
    print('Os dois números são iguais!!')
