#O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem dos sorteados.

from random import shuffle
a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
list = [a, b, c, d]
shuffle(list)
print('A ordem de apresentação será {}'. format(list))
