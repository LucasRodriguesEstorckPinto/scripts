import random
from time import sleep


nome = input('Digite seu nome de usuário: ').strip().lower().capitalize()
a = str(input('Escolha entre pedra, papel ou tesoura: ')).strip().upper()
b = ('PEDRA', 'PAPEL', 'TESOURA')
c = random.choice(b)

if a == c:
    print('JÔ')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    print('-=' * 11)
    print(f'A máquina escolheu {c}')
    print('Empate')
    print('-=' * 11)

elif a == 'PEDRA' and c == 'PAPEL' or a == 'TESOURA' and c == 'PEDRA' or a == 'PAPEL' and c == 'TESOURA':
    print('JÔ')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    print('-=' * 11)
    print(f'A máquina escolheu {c}')
    print('Vitória da máquina')
    print('-=' * 11)
else:
    print('JÔ')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    print('-=' * 11)
    print(f'A máquina escolheu {c}')
    print(f'Vitória de {nome}!! ')
    print('-=' * 11)
