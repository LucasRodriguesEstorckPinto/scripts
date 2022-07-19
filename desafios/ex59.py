from time import sleep
r = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
h = [n1, n2]
while r != 5:
    if r == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        h = [n1, n2]
    print(''
          '[1] SOMAR\n'
          '[2] MULTIPLICAR\n'
          '[3] MAIOR\n'
          '[4] NOVOS NÚMEROS\n'
          '[5] SAIR DO PROGRAMA\n')
    r = int(input('>>>>Sua escolha: '))
    if r == 1:
        print('-=' * 10)
        print(f'\033[31m     {n1}+{n2} = {n1 + n2}\033[m')
        print('-=' * 10)
    elif r == 2:
        print('-=' * 10)
        print(f'\033[31m     {n1}x{n2} = {n1 * n2}\033[m')
        print('-=' * 10)
    elif r == 3:
        print('-=' * 20)
        print(f'\033[31m     O maior número entre {n1} e {n2} é: {max(h)}\033[m')
        print('-=' * 20)
    if r > 5 or r == 0 or r < 0:
        print('HAHAHAHHAHAHA RETARDADO BOTA O VALOR CERTO')
        print('=-=' * 16)
    sleep(1)
print('_' * 15)
print('Finalizando...')
sleep(1)
print('Programa finalizado')
