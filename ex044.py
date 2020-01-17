#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento: - à vista dinheiro/cheque: 10% de desconto. - à vista no cartão: 5% de desconto. -em até 2x no cartão: preço normal. -3x ou mais no cartão: 20% de juros simples.

v = float(input('Digite o preço do produto: R$ '))
p = str(input('Digite a forma de pagamento desejada (cartao, cheque ou dinheiro): ')).lower()
if p == 'cartao' or p == 'cheque' or p == 'dinheiro':
  if p =='dinheiro' or p == 'cheque':
      f = v-(v*0.1)
      print('A forma de pagamento escolhido é {}, o valor à pagar, com o desconto de 10% é de R$ {}'.format(p, f))
  elif p == 'cartao':
      j = str(input('Digite a forma de parcelamento do cartão (a vista, 2x, 3x ou mais): ')).lower()
      if j == 'a vista':
          f = v-(v*0.05)
          print('A forma de pagamento escolhida é cartão à vista, o valor à pagar com o desconto de 5% é de R$ {}'.format(f))
      elif j == '2x':
          print('A forma de pagamento escolhida é cartão parcelado em 2x, o valor à pagar é de R$ {}'.format(v))
      elif j == '3x' or j == 'mais':
          f = v + (v * 0.2)
          print('A forma de pagamento escolhida é parcelado em 3x ou mais, o valor à pagar com juros de 20% é de R$ {}'.format(f))
      else:
          print('A forma de parcelamento escolhida é inválida')
else:
  print('A forma de pagamento escolhida é inválida')
