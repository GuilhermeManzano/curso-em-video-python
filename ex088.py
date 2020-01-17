# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista completa.

from random import sample
from time import sleep
jogos = list()
n = int(input('Quantos jogos você quer?: '))
for c in range(n):
    a = sorted(sample(range(1, 61), 6))
    jogos.append(a[:])
    print(f'Jogo {c+1}: {a}')
    sleep(0.5)
