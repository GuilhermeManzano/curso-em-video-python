#Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da pasagem, cobrando R$0,50 por KM nas viagens de até 200 KM e R$ 0,45 para viagens mais longas.

d = int(input('Qual a distância percorrida da viagem (em KM)?: '))
if d <= 200:
    x = d*.5
    print('Você irá pagar R$ {} pela passagem.'.format(x))
else:
    x = d*0.45
    print('Você irá pagar R$ {} pela passagem.'.format(x))
