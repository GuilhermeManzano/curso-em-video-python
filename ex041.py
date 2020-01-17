#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: - Até 9 anos: MIRIM. - Até 14 anos: INFANTIL. -Até 19 anos: JUNIOR. -Até 40 anos: SÊNIOR. -Acima: MASTER

i = int(input('Digite a idade do aluno: '))
if i <= 9:
    print('\033[1;30m O aluno é da categoria MIRIM \033[m')
elif 9 < i <= 14:
    print('\033[1;31m O aluno é da categoria INFANTIL \033[m')
elif 14 < i <= 19:
    print('\033[1;35m O aluno é da categoria JÚNIOR \033[m')
elif 19 < i < 40:
    print('\033[1;33m O aluno é da categoria SÊNIOR \033[m')
elif i >= 40:
    print('\033[1;36m O aluno é da categoria MASTER \033[m')
