# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

n = int(input('Em que ano você nasceu?: '))
p = 2019 - n
if p == 18:
    print('Quem nasceu em {} tem 18 anos em 2019'.format(n))
    print('\033[7;30m Você tem que se alistar IMEDIATAMENTE! \033[m')
elif p < 18:
    print('Quem nasceu em {} tem {} anos em 2019'.format(n, p))
    print('Ainda falta(m) {} ano(s) para seu alistamento'.format(18-p))
    print('\033[4;33;41m Seu alistamento será em {} \033[m'.format(2019+18-p))
else:
    print('Quem nasceu em {} tem {} anos em 2019'.format(n, p))
    print('Você deveria ter se alistado há {} anos'.format(p-18))
    print('\033[1;33;47m Seu alistamento foi em {} \033[m'.format(n+18))
