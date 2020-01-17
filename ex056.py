# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: -A média de idade do grupo. -Qual é o nome do homem mais velho. -Quantas mulheres têm menos de 20 anos.

som = 0
maior = 0
velho = 0
idvelho = 0
totm = 0
for c in range(1, 5):
    print('------ {}° pessoa -----'.format(c))
    n = str(input('Nome: ')).upper()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).upper()
    som += i
    if c == 1 and s == 'M':
        idvelho = i
        velho = n
    if s == 'M' and i > idvelho:
        idvelho = i
        velho = n
    if s == 'F' and i < 20:
        totm += 1
print('A média de idade do grupo é de {} anos'.format(som/4))
print('O homem mais velho tem {} anos e se chama {}'.format(idvelho, velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totm))
