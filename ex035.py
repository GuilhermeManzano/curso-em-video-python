# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('\033[0;31;43m Digite o comprimento da primeira reta:\033[m '))
b = float(input('\033[1;36;47m Digite o comprimento da segunda reta:\033[m '))
c = float(input('\033[7;30m Digite o comprimento da terceira reta:\033[m '))
if ((abs(b - c)) < a < (b + c)) or ((abs(a - c)) < b < (a + c)) or ((abs(a - b)) < c < (a + b)):
    print('As três retas podem formar um triângulo!')
else:
    print('As três retas NÃO podem formar um triângulo!')
