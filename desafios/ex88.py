from random import randint
from time import sleep
palpite = []
print('=='*20)
print(f'{"JOGO DA MEGA SENA":^40}')
print('=='*20)
pa = int(input('Quantos jogos você vai jogar? '))
print(f'======SORTEANDO {pa} JOGOS======')
dado = []
for c in range(0,pa):
    while len(dado)<6:
        h = randint(1,60)
        if h not in dado:
            dado.append(h)
    palpite.append(dado[:])
    dado.clear()
for c in range(0,pa):
    print(f'Jogo {c+1}: {palpite[c]}')
    sleep(1)
print('BOA SORTE!! ')
