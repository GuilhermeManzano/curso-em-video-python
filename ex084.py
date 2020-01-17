# Faça um programa que leia nome e peso de vários pesoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) Uma listagem com mais pessoas. C) Uma listagem com as pesoas mais leves.

temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    cont = str(input('Você deseja adicionar outro valor? [S/N] ')).upper()
    if cont in 'Nn':
        break
print(f'Ao todo, você cadastrou {len(princ)}')
print(f'O MAIOR peso foi de {maior} kg.', end='')
for p in princ:
    if p[1] == maior:
        print(f'  {p[0]} ', end='')
print()
print(f'O MENOR peso foi de {menor} kg.', end='')
for p in princ:
    if p[1] == menor:
        print(f'  {p[0]} ', end='')
print()
