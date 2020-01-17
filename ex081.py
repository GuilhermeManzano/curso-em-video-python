# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma crescente. C) Se o valor 5 foi digitado e está ou não na lista.

valores = list()
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    print('Valor adicionado com sucesso')
    cont = str(input('Você deseja adicionar outro valor? [S/N] ')).upper()
    if cont in 'Nn':
        break
print(f'Você digitou {len(valores)} valores')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescentes são: {valores}')
if 5 in valores:
   print('O valor 5 faz parte da sua lista')
else:
   print('O valor 5 não faz parte de sua lista')
