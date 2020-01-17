# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá  dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente.

valores = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
       valores.append(n)
       print('Valor adicionado com sucesso')
    else:
       print('Valor duplicado! Não vou adicionar...')
    cont = str(input('Você deseja adicionar outro valor? [S/N] ')).upper()
    if cont in 'Nn':
        break
valores.sort()
print('Você digitou os valores {}'.format(valores))
