# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listras extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

valores = list()
par = list()
impar = list()
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    print('Valor adicionado com sucesso')
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    cont = str(input('Você deseja adicionar outro valor? [S/N] ')).upper()
    if cont in 'Nn':
        break
print(f'A lista completa é: {valores}')
par.sort()
impar.sort()
print(f'A lista de números pares é: {par}')
print(f'A lista números ímpares é: {impar}')
