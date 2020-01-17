#Crie um programa que leia o nome de uma cidade e diga se começa ou não com o nome "SANTO"

cit = str(input('Digite o nome de uma cidade: '))
p = cit.title()
q = p.strip()
print('{}'.format('Santo' in q))
