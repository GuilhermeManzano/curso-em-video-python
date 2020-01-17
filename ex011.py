# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2 m².

lar = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
a = lar * alt
t = a/2
print('A largura é de {} m e a altura é de {} m \n A sua área é de {} m²'.format(lar, alt, a))
print('Será necessário {} l de tinta para pintar toda a parede'.format(t))
