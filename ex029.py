# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7 por cada KM acima do limite.

v = int(input('Qual é a velocidade do carro?: '))
if v > 80:
    v = v
else:
    x = (v - 80)*7
    print('Você está acima da velocidade máxima e foi multado em R$ {}'.format(x))
