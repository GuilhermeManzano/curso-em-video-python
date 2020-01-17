# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    med = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], med])
    cont = str(input('Você deseja adicionar outro valor? [S/N] ')).upper()
    if cont in 'Nn':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-='*13)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    show = int(input('Mostrar notas de qual aluno? (999 para parar): '))
    if show == 999:
        break
    if show <= len(ficha)-1:
        print('-=' * 13)
        print(f'Notas de {ficha[show][0]} são: {ficha[show][1]}')
print('Obrigado por utilizar nosso programa!')
