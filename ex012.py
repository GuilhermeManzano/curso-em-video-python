# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

n = float(input('Qual é o preço do produto? R$ '))
d = n*.95
print('O produto que custava R$ {}, na promoção com 5% de desconto vai custar R$ {}'.format(n, d))
