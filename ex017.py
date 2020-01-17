# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math
co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
h = math.sqrt(math.pow(co, 2) + math.pow(ca, 2))
print('O valor da Hipotenusa é de: {}'.format(h))
