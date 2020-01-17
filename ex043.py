#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela: - Abaixo de 18,5: Abaixo do peso. - Entre 18,5 e 25: Peso Ideal. - 25 até 30: Sobrepeso. - 30 até 40: Obesidade. - Acima de 40: Obesidade mórbida.

from math import ceil
p = float(input('Digite o seu peso em KG: '))
a = float(input('Digite a sua altura em metros: '))
imc = p/(a*a)
if imc <= 18.5:
    print('O seu IMC é {} e você está ABAIXO DO PESO'.format(ceil(imc)))
if 18.5 < imc <= 25:
    print('O seu IMC é {} e você está no PESO IDEAL!! Continue assim!'.format(ceil(imc)))
if 25 < imc <= 30:
    print('O seu IMC é {} e você está com SOBREPESO'.format(ceil(imc)))
if 30 < imc <= 40:
    print('O seu IMC é {} e você está OBESO(A)'.format(ceil(imc)))
if imc > 40:
    print('O seu IMC é {} e você está com OBESIDADE MÓRBIDA'.format(ceil(imc)))
