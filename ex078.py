# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.

maior = menor = 0
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        elif valores[cont] < menor:
            menor = valores[cont]
for c, v in enumerate(valores):
    print(f'Na posição {c} está o valor {v}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
