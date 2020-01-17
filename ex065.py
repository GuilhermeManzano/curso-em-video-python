# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execuçao, mostre a media entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores.

resp = 'S'
soma = count = maior = menor = 0

while resp in 'Ss':
    n = int(input('Digite um valor: '))
    soma += n
    count += 1
    if count == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] '))
media = soma/count
print('Você digitou {} valores e a media entre eles é {}'.format(count, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
