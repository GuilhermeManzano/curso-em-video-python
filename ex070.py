# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuario vai continuar. No final, mostre: A) Qual é o total gasto na compra. B) Quantos produtos custam mais de R$ 1000. C) Qual é o nome do do produto mais barato.

v = barato = caro = tot = 0
nome = ' '
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = int(input('Preço: R$ '))
    v += 1
    tot += preco
    cont = ' '
    if preco > 1000:
        caro += 1
    if v == 1:
        barato = preco
        nome = produto
    else:
        if preco < barato:
            barato = preco
            nome = produto
    while cont not in 'SN':
        cont = str(input('Quer continuar?: [S/N]')).upper().strip()[0]
    print('{:-^40}'.format('  FIM '))
    if cont == 'N':
        break
print(f'O total gasto na compra foi de R$ {tot:.2f} \n{caro} produtos custam mais de R$ 1000 \nO nome do produto mais barato é {nome}')