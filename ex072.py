# Crie um programa que tenha uma tupia totalmente preenchido com uma contagem por extenso, de zero até vinte. Seu programa deverá ter ter um número pelo teclado (entre 0 e 20) e mostrá-la por extenso.

n = int(input('Digite um número entre 0 e 20: '))
if n <= 20:
    esc = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    print(f'Você digitou o número {esc[n-1]}')
else:
    while n > 20:
      n = int(input('Digite um número entre 0 e 20: '))
