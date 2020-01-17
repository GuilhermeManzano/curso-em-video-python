# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

alunos = dict()
alunos['nome'] = str(input('Digite o nome do aluno: '))
alunos['media'] = float(input(f'Digite a média de {alunos["nome"]}: '))
if alunos['media'] < 5:
    alunos['situacao'] = 'Reprovado'
else:
    alunos['situacao'] = 'Aprovado'
for k, v in alunos.items():
    print(f'{k} é igual {v}')
