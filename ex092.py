# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionario também receberá o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos vai se aposentar.

from datetime import datetime

carteira = dict()
while True:
    carteira['nome'] = str(input('Nome: '))
    carteira['nasc'] = int(input('Ano de Nascimento: '))
    carteira['idade'] = 2019 - carteira['nasc']
    carteira['cpts'] = int(input('Carteira de Trabalho (digite 0 se não possui): '))
    if carteira['cpts'] == 0:
        del carteira['nasc']
        for k, v in carteira.items():
            print(f'   - {k} tem o valor {v}')
        break
    else:
        carteira['contratação'] = int(input('Ano de contratação: '))
        carteira['salario'] = float(input('Salário: R$ '))
        del carteira['nasc']
        carteira['aposentadoria'] = ((carteira['contratação'] + 35) - datetime.now().year)
        for k, v in carteira.items():
            print(f'   - {k} tem o valor {v}')
