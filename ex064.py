# Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar 999, que é a condição final de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando a flag)

cont = soma = 0
n = int(input('Digite um número (digite 999 para parar): '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número (digite 999 para parar): '))
print('Você digitou {} números e a soma deles é: {}'.format(cont, soma))
