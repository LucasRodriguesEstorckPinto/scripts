from random import randint
t1 = (randint(0,10), randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f'Os 5 números sorteados foram: ',end='')
for c in range(0,5):
    print(f'{t1[c]}',end=' ')
print(f'\nO maior valor sorteado foi {max(t1)}')
print(f'O menor valor sorteado foi {min(t1)}')