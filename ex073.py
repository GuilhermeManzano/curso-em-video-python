# Crie uma tupla com os 20 primeiros colocados do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: A) apenas os 5 primeiros colocados. B) Os últimos 4 colocados da tabela. C) Uma lista com os times em ordem alfabética. D) Em que posição da tabela está o time Chapecoense.

print('-=' * 20)
times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná')

print(f'Lista de times do Brasileirão: {times}')
print('-=' * 20)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 20)
print(f'Os 4 últimos são: {times[16:20]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 20)
print('O Chapecoense está na posição: {}°'.format(times.index("Chapecoense")))
print('-=' * 20)
