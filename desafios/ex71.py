print('=' * 30)
print('{:^30}'.format('BANCO ESTORCK'))
print('=' * 30)
val = int(input('Qual valor você deseja sacar? R$ '))
total = val
ced = 50
cont = 0
while True:
    if total>=ced:
        total = total - ced
        cont = cont + 1
    else:
        if cont>0:
            print(f'Total de {cont} cédulas de R${ced}')
        if ced==50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced==10:
            ced = 1
        cont = 0
        if total==0:
            break

