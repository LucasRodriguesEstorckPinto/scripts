n = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão da PA: '))
print('----Serão mostrados os 10 primeiros números dessa PA----')
f = n +(10-1)*r
for c in range(n,f+1,r):
    print(c,end=' - ')
print('FIM',end=' ')