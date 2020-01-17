#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolhe qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: \n \033[0;34m [ 1 ] converter para BINÁRIO \033[m')
print('\033[1;32m  [ 2 ] converter para OCTAL \033[m \n \033[0;30m [ 3 ] converter para HEXADECIMAL \033[m')
o = int(input('Sua opção: '))
if o == 1:
   print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)))
elif o == 2:
   print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)))
elif o == 3:
   print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)))
else:
    print('Opção inválida, escolha uma opção entre 1 e 3')
