from time import sleep


def helpa(d):
    linha(f'Acessando manual da função "{d}" ')
    sleep(1)
    print('\033[7;40m')
    help(d)
    print('\033[m')


def linha(msg):
    tam = len(msg) + 4
    print('\033[30;43m')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print('\033[m')


while True:
    sleep(0.7)
    linha('SISTEMA DE AJUDA PyHELP')
    res = str(input('help> ')).strip().lower()
    if res.upper() == 'FIM':
        break
    helpa(res)

print('Programa finalizado :)')
