# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuario qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possua cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.

while True:
    valor = int(input('Qual valor você quer sacar? R$ '))
    cin = valor // 50
    valor %= 50
    vin = valor // 20
    valor %= 20
    dez = valor // 10
    valor %= 10
    um = valor // 1
    valor %= 1
    break
print('-' * 30)
print(f'Total de {cin} cédulas de R$ 50 \nTotal de {vin} cédulas de R$ 20')
print(f'Total de {dez} cédulas de R$ 10 \nTotal de {um} cédulas de R$ 1')
print('-' * 30)
print('Volte sempre. Tenha um bom dia!')
