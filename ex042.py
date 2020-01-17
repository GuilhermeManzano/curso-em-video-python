# Refaça o DESAFIO 35 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado: - Equilátero, Isósceles ou Escaleno.

a = float(input('\033[0;31;43m Digite o comprimento da primeira reta:\033[m '))
b = float(input('\033[1;36;47m Digite o comprimento da segunda reta:\033[m '))
c = float(input('\033[7;30m Digite o comprimento da terceira reta:\033[m '))
if ((abs(b - c)) < a < (b + c)) or ((abs(a - c)) < b < (a + c)) or ((abs(a - b)) < c < (a + b)):
    if a == b == c:
        print('As três retas podem formar um triângulo \033[1;33;45m EQUILÁTERO! \033[m')
    elif a == b or a == c or b == c:
        print('As três retas podem formar um triângulo \033[7;36;42m ISÓSCELES! \033[m')
    else:
        print('As três retas podem formar um triângulo \033[1;30;42m ESCALENO! \033[m')
else:
    print('As três retas NÃO podem formar um triângulo!')
