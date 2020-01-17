# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuario quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) Quantos homens foram cadastrados. C) Quantas mulheres tem menos de 20 anos.

velho = h = m = 0
while True:
  print('Cadastre uma pessoa \n --------------------')
  idade = int(input('Digite a idade: '))
  if idade > 18:
     velho += 1
  sexo = ' '
  while sexo not in 'MF':
     sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
  if sexo == 'M':
     h +=1
  cont = ' '
  if sexo == 'F' and idade < 20:
      m += 1
  while cont not in 'SN':
      cont = str(input('Quer continuar?: [S/N]')).upper().strip()[0]
  if cont == 'N':
      break
  print('---------------------')
print(f'{velho} pessoas tem mais de 18 anos \n{h} homens foram cadastrados \n{m} mulheres tem menos de 20 anos')
