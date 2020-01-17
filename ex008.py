#Escreva um programa que leia um número em metros e o exiba convertido em centímetros e milímetros.

n = int(input('Digite um valor em metros: '))
cm = 100*n
mm = 1000*n
km = n/1000
print('O valor digitado em metros foi: {} m \nO valor em centímetros é: {} cm \nO valor em milímetros é: {} mm \nO valor em quilômetros é {} km'.format(n, cm, mm, km))

