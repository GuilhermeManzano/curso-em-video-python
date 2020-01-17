# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) A média de idade do grupo. C) Uma lista com todas as mulheres. D) Uma lista com todas as pessoas com idade acima da média.

pessoas = dict()
galera = list()
soma = med = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper()
        if pessoas['sexo'] in 'mfMF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        continuar = str(input('Você quer continuar? [S/N] ')).upper()
        if continuar in 'SsNn':
            break
        print('ERRO! Por favor, digite apenas S ou N')
    if continuar == 'N':
        break
print('-'*60)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
med = soma/len(galera)
print(f'B) A média de idade do grupo é de {med:5.2f} anos.')
print('C) As mulheres cadastradas foram:', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('D) Lista das pessoas que estão acima da média:', end=' ')
for p in galera:
    if p['idade'] >= med:
        print(p['nome'], end=' ')
