# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a digitação novamente até um ter o valor correto.


n = str(input('Informe seu sexo:[M/F] ')).upper().strip()
while n != 'M' and n != 'F':
    n = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip()
print('Sexo {} registrado com sucesso'.format(n))
