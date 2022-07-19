l = []
while True:
    p =int(input('Digite um valor: '))
    if p in l:
        print('valor duplicado! Não será contabilizado')
    else:
        print('Valor adicionado com sucesso!!')
        l.append(p)
    r = 'f'
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('='*30)
print('Você digitou os números: ', end='')
l.sort()
for n in l:
    print(f'{n}... ',end='')
