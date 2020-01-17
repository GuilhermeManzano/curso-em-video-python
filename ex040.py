# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingica: - abaixo de 5.0 = reprovado. -entre 5 e 6.9 = recuperação. -7 pra cima = aprovado.

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1 + n2)/2
if m < 5:
    print('O aluno obteve uma nota média de {} e foi\033[1;31m REPROVADO \033[m'.format(m))
elif 5 <= m <= 6.9:
    print('O aluno obteve uma nota média de {} e ficou em\033[1;34m RECUPERAÇÃO \033[m'.format(m))
elif m > 7:
    print('O aluno obteve uma nota média de {} e foi\033[7;35m APROVADO \033[m'.format(m))
