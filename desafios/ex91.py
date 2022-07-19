from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
print('Valores sorteados')
for c, j in jogadores.items():
    print(f'O {c} tirou {j} no dado')
    sleep(1)
print('==' * 20)
print('ranking dos jogadores')
ordem = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for c in range(0, 4):
    print(f'{c + 1}° lugar: {ordem[c][0]} com {ordem[c][1]}')
