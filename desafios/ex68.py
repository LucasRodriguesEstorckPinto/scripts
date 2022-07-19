from random import randint
v = 0
while True:
    print('_'*20)
    print('PAR OU IMPAR')
    print('_'*20)
    h = randint(0, 10)
    n = str(input('[P] PAR [I] IMPAR: ')).strip().upper()[0]
    while n not in 'PI':
        n = str(input('[P] PAR [I] IMPAR: ')).strip().upper()[0]
    n1 = int(input('Seu número: '))
    s = h + n1
    print('=-' * 10)
    if n=='P' or n=='I':
        if s % 2 == 0:
            print(f'Você jogou {n1} e o computador {h}. Total de {s} DEU PAR')
        if s % 2 == 1:
            print(f'Você jogou {n1} e o computador {h}. Total de {s} DEU IMPAR')
        print('=-'*20)
        if n == 'P' and s % 2 == 0 or n == 'I' and s % 2 == 1:
            print('VOCÊ VENCEU!!')
            v = v + 1
        else:
            print('VOCÊ PERDEU')
            break
print('=-'*20)
print(f'GAME OVER. Você venceu {v} vezes')
