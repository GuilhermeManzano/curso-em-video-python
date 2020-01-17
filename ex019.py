# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome do escolhido.

from random import choice
a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
r = choice([a, b, c, d])
print('O aluno escolhido foi {}'.format(r))
