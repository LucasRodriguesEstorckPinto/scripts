r = 'j'
li = []
c = 0
while True:
    li.append(int(input('Digite um número: ')))
    c = c + 1
    r = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('DIGITE CORRETAMENTE - Deseja continuar? [S/N]')).strip().upper()[0]
    if r in 'N':
        print('Exibindo resultados')
        break
print('='*60)
print(f'FORAM DIGITADOS {c} NÚMEROS')
li.sort(reverse=True)
print('Os números em ordem decrescente fica da seguinte maneira: ',end=' ')
for n in li:
    print(n,end='  ')
if 5 in li:
    print(f'\nO número 5 foi digitado e faz parte da lista')
else:
    print('\nO número 5 não foi digitado')
