# Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
for c in range(1, 501, 2):
  x = c % 3
  if x == 0:
   soma = soma + c #Função acumulador, a cada volta irá adicionar mais um número na soma.
print('A soma dos números é: {}'.format(soma))
