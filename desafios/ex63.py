print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)
f = int(input('Quantos termos você quer mostrar? : '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} >> {t2}', end='')
c = 3
while c <= f:
    t3 = t1 + t2
    print(f' >> {t3}', end='')
    t1 = t2
    t2 = t3
    c = c + 1
