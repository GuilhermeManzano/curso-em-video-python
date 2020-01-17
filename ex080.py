# Crie um programa onde o usuário possa digitar cinco valors numéricos e cadastre-os em uma lista, já na posição correta da inserção(sem usar o sort()). No final, mostre a lista ordenada na tela.

valores = []
pos = 0
for c in range(0, 5):
   n = int(input('Digite um valor: '))
   if n not in valores:
      if c == 0:
         valores.append(n)
         print('Valor adicionado com sucesso')
      elif n > valores[len(valores)-1]: # pega o ultimo elemento da lista para comparar
          valores.append(n)
          print('Valor adicionado com sucesso')
      else:
          pos = 0
          while pos < len(valores):
              if n <= valores[pos]:
                  valores.insert(pos, n)
                  print('Valor adicionado com sucesso')
                  break
              pos +=1
   else:
      print('Valor duplicado! Não vou adicionar...')
print(f'Os valores digitados em ordem foram {valores}')
