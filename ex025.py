#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

n = str(input('Digite o seu nome completo: '))
p = n.title()
q = p.strip()
print('Seu nome tem Silva? {}'.format('Silva' in q))
