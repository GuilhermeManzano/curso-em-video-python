# Aprimore o DESAFIO 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização detalhada de aproveitamento de cada jogador.

jogador = dict()
gols = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear()
    for p in range(0, partidas):
        gols.append(int(input(f'    Quantos gols na partida {p}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    continuar = str(input('Você quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print('=-'*40)
print('cod  ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*80)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*80)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Não existe jogador com este código')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR  {time[busca]["nome"]} -- ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols')
    print('-'*40)
print('-- Volte Sempre --')
