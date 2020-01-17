# Crie um pograma que leia dois valores e mostre um menu na tela: [1] somar; [2] multiplicar; [3] maior; [4] novos numeros; [5] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
print('[1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa')
op = int(input('>>> Qual é a sua opção? :'))
while op != 5:
   if op == 1:
      s = n1 + n2
      print('A soma dos números é: {}'.format(s))
      print('[1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa')
      op = int(input('>>> Qual é a sua opção? :'))
   elif op == 2:
      m = n1 * n2
      print('A multiplicação dos itens é: {}'.format(m))
      print('[1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa')
      op = int(input('>>> Qual é a sua opção? :'))
   elif op == 3:
       if n1 > n2:
           print('O maior número é: {}'.format(n1))
           print('[1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa')
           op = int(input('>>> Qual é a sua opção? :'))
       else:
           print('O maior número é: {}'.format(n2))
           print('[1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa')
           op = int(input('>>> Qual é a sua opção? :'))
   elif op == 4:
      n1 = int(input('Digite o 1° valor: '))
      n2 = int(input('Digite o 2° valor: '))
      print('[1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa')
      op = int(input('>>> Qual é a sua opção? :'))
print('Fim do programa')
