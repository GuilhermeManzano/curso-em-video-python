# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.

math = [[], []]
for n in range(0, 7):
    numb = int(input(f'Digite o {n+1}° valor: '))
    if numb % 2 == 0:
        math[0].append(numb)
    else:
        math[1].append(numb)
print('-'*30)
math[0].sort()
math[1].sort()
print(f'Os números pares são: {math[0]}')
print(f'Os números pares são: {math[1]}')
