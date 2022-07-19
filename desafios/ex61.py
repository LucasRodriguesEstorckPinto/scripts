n = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão da PA: '))
c = 0
print('----Serão mostrados os 10 primeiros números dessa PA----')
while c <=10:
    n = n + r
    c = c + 1
    if c <=10:
        print(f' {n} ', end=' ')
