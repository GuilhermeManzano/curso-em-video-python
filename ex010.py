# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quandos dólares ela pode comprar com esse dinheiro.

n = float(input('Quanto dinheiro você tem na carteira?: R$ '))
print('Com R$ {} é possível comprar US$ {}'.format(n, n*3.27))
