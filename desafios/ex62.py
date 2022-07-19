n = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão da PA: '))
c = 0
h = 10
j = 0
print('----Serão mostrados os 10 primeiros números dessa PA----')
while h!=0:
    while c <=j:
        j = j + h
        n = n + r
        c = c + 1
        if c <= 10:
            print(f' {n} ', end=' ')
    h = int(input(('\nQuantos termos a mais deseja colocar? ')))
print('fim')


