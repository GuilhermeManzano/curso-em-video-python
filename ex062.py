# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra a quando ele disser que quer mostrar 0 termos.

n = int(input('Digite o primeiro termo de um PA: '))
r = int(input('Digite a razão da PA: '))
pa = n
mais = 10
v = 1
tot = 0
print('Calculando a PA de {}'.format(n))
while mais != 0:
    tot = tot + mais
    while v <= tot:
        print('{}'.format(pa), end=' -> ')
        v += 1
        pa = n + r * v
    print('PAUSA')
    mais = int(input('\n Quantos mais termos você deseja exibir? '))
print('Progressão finalizada com {} termos mostrados'.format(tot))
