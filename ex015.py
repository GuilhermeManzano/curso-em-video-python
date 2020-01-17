# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por KM rodado.

qt = float(input('Quantos quilômetros foram rodados?: '))
d = int(input('Quantos dias o carro foi utilizado?: '))
t = qt*0.15 + d*60
print('O total a ser pago é de R$ {}'.format(t))